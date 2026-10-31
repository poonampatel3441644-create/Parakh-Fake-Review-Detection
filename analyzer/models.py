from django.db import models


class Analysis(models.Model):
    session_key = models.CharField(max_length=40, db_index=True)
    review = models.TextField()
    genuine_pct = models.PositiveSmallIntegerField()
    verdict = models.CharField(max_length=10)
    sentiment = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "analyses"

    @property
    def verdict_label(self):
        return {
            "genuine": "Genuine style",
            "machine": "Machine-written style"
        }.get(self.verdict, "Not clear")

    @property
    def preview(self):
        return self.review if len(self.review) <= 140 else self.review[:140] + "…"

    def __str__(self):
        return f"{self.verdict} ({self.genuine_pct}%) {self.created_at:%d %b %Y}"