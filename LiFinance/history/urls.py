from django.urls import path

from . import views

app_name = "history"
url_patterns = [
    path('', views.history, name="history"),
]

