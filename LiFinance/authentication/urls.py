from django.urls import path, include

from django.views.generic import RedirectView

from django.contrib.auth import views as authViews

from . import views

app_name = "authentication"
urlpatterns = [
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
    path('', include('django.contrib.auth.urls')),
]