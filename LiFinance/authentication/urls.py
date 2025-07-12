from django.urls import path, include

from . import views

app_name = "authentication"
urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('account/', views.account_view, name="account"),
    path('account/add_category', views.add_category, name="add_category"),
    path('account/add_bank_account', views.add_bank_account, name="add_bank_account"),
    path('account/delete_category/<int:category_id>', views.delete_category, name="delete_category"),
    path('account/delete_bank_account/<int:bank_account_id>', views.delete_bank_account, name="delete_bank_account"),
    path('account/update_category/<int:category_id>', views.update_category, name="update_category"),
    path('account/update_bank_account/<int:bank_account_id>', views.update_bank_account, name="update_bank_account"),
    
    path('', include('django.contrib.auth.urls')),
]