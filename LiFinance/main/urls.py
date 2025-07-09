from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path('', views.index, name="index"),
    path('add_cheque', views.add_cheque, name="add_cheque"),
    path('add_cheque/add_content', views.add_content, name="add_content"),
]