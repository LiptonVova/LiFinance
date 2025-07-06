from django.urls import path, include

from . import views

app_name = "authentication"
urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('', include('django.contrib.auth.urls')),
]