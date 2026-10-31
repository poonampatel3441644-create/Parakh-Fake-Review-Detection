from django.urls import path
from . import views

urlpatterns = [
    path("", views.analyze_review, name="analyze_review"),
    path("history/", views.history, name="history"),
    path("history/clear/", views.clear_history, name="clear_history"),
]