from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path('', views.index, name="index"),
    path('add_cheque', views.add_cheque, name="add_cheque"),
    path('delete_cheque/<int:cheque_id>', views.delete_cheque, name="delete_cheque"),
    path('update_cheque/<int:cheque_id>', views.update_cheque, name="update_cheque"),
]