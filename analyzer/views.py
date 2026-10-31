from pathlib import Path

import joblib
import numpy as np
from django.shortcuts import redirect, render
from .models import Analysis

BASE_DIR = Path(__file__).resolve().parent.parent
authenticity_model = joblib.load(BASE_DIR / "models" / "authenticity_model.joblib")
sentiment_model = joblib.load(BASE_DIR / "models" / "sentiment_model.joblib")

STRONG = 0.65          # heuristic cut-off, not a calibrated confidence
MAX_CHARS = 3000
SENTIMENT_ORDER = ["negative", "neutral", "positive"]


def verdict(or_prob):
    if or_prob >= STRONG:
        return "genuine", "Looks genuine"
    if or_prob <= 1 - STRONG:
        return "machine", "Looks machine-written"
    return "unclear", "Can't tell"


def influential_words(text, top_n=5):
    vec = authenticity_model.named_steps["tfidf"]
    clf = authenticity_model.named_steps["classifier"]
    cleaned = authenticity_model.named_steps["preprocessing"].transform([text])
    x = vec.transform(cleaned)
    contrib = x.multiply(clf.coef_[0]).toarray()[0]
    names = vec.get_feature_names_out()
    order = np.argsort(contrib)
    genuine = [names[i] for i in order[::-1][:top_n] if contrib[i] > 0]
    machine = [names[i] for i in order[:top_n] if contrib[i] < 0]
    return genuine, machine


def build_result(review):
    classes = list(authenticity_model.classes_)
    or_prob = float(authenticity_model.predict_proba([review])[0][classes.index("OR")])
    key, headline = verdict(or_prob)
    genuine_words, machine_words = influential_words(review)

    s_probs = dict(zip(sentiment_model.classes_,
                       sentiment_model.predict_proba([review])[0]))
    top = max(s_probs, key=s_probs.get)
    sentiment_label = top.capitalize() if s_probs[top] >= 0.5 else "Mixed"

    genuine_pct = round(or_prob * 100)
    return {
        "key": key,
        "headline": headline,
        "genuine_pct": genuine_pct,
        "machine_pct": 100 - genuine_pct,
        "genuine_words": genuine_words,
        "machine_words": machine_words,
        "sentiment_label": sentiment_label,
        "sentiment_rows": [
            {"name": c.capitalize(), "pct": round(float(s_probs[c]) * 100)}
            for c in SENTIMENT_ORDER
        ],
        "short": len(review.split()) < 8,
    }


def _session_key(request):
    if not request.session.session_key:
        request.session.create()

    return request.session.session_key


def analyze_review(request):
    context = {"review": "", "result": None, "error": None}

    if request.method == "POST":
        review = request.POST.get("review", "").strip()[:MAX_CHARS]
        context["review"] = review

        if len(review.split()) < 3:
            context["error"] = (
                "Enter at least a full sentence so Parakh has something to read."
            )
        else:
            try:
                result = build_result(review)

            except Exception:
                context["error"] = (
                    "Parakh couldn't analyze that text. Try a different review."
                )

            else:
                context["result"] = result

                Analysis.objects.create(
                    session_key=_session_key(request),
                    review=review,
                    genuine_pct=result["genuine_pct"],
                    verdict=result["key"],
                    sentiment=result["sentiment_label"],
                )

    return render(request, "analyzer/index.html", context)


def history(request):
    key = request.session.session_key

    items = (
        list(Analysis.objects.filter(session_key=key)[:50])
        if key else []
    )

    return render(
        request,
        "analyzer/history.html",
        {"items": items}
    )


def clear_history(request):
    if request.method == "POST" and request.session.session_key:
        Analysis.objects.filter(
            session_key=request.session.session_key
        ).delete()

    return redirect("history")