from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import CategoryModelForm, BankAccountModelForm
from main.models import Category, BankAccount

from django.forms import modelform_factory

from django.contrib.auth.decorators import login_required

@login_required(login_url=reverse_lazy("authentication:login"))
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("authentication:login"))


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]        
            User.objects.create_user(username=username, password=password)            
            return HttpResponseRedirect(reverse("authentication:login"))
    
    else:
        form = UserCreationForm()
        
    return render(request, "registration/register.html", {"form": form}) 


@login_required(login_url=reverse_lazy("authentication:login"))
def account_view(request):
    form_category = CategoryModelForm()
    form_bank_account = BankAccountModelForm()
    
    context = {
        "form_category": form_category,
        "form_bank_account": form_bank_account,        
    }       
    return render(request, "registration/account.html", context=context)


@login_required(login_url=reverse_lazy("authentication:login"))
def add_category(request):
    form_category = CategoryModelForm(request.POST)
    if form_category.is_valid():
        new_category = Category()
        new_category.name = form_category.cleaned_data["name"]
        new_category.category_type = form_category.cleaned_data["category_type"]
        new_category.user = request.user
        
        new_category.save()
        
    return HttpResponseRedirect(reverse("authentication:account"))
    
    
@login_required(login_url=reverse_lazy("authentication:login"))
def add_bank_account(request):
    form_bank_account = BankAccountModelForm(request.POST)
    if form_bank_account.is_valid():
        name = form_bank_account.cleaned_data["name"]
        bank_account = BankAccount(name=name, user=request.user)
        
        bank_account.save()
        
    return HttpResponseRedirect(reverse("authentication:account"))