from django.urls import path, include

from . import views

app_name = "authentication"
urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('account/', views.account_view, name="account"),
    path('account/add_category', views.add_category, name="add_category"),
    path('account/add_bank_account', views.add_bank_account, name="add_bank_account"),
    path('', include('django.contrib.auth.urls')),
]