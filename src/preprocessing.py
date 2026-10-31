
import re


def drop_trailing_fragment(text):
    """Remove text after the last sentence-ending punctuation mark."""
    text = re.sub(r"([.!?])([A-Za-z])", r"\1 \2", str(text))

    if re.search(r"[.!?]", text):
        text = re.sub(r"[^.!?]*$", "", text)

    return re.sub(r"\s+", " ", text).strip()


def clean_texts(texts):
    """Apply the preprocessing function to a collection of reviews."""
    return [drop_trailing_fragment(text) for text in texts]
