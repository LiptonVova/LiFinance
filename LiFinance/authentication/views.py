from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import CategoryModelForm, BankAccountModelForm
from main.models import Category, BankAccount, Operation

from django.contrib import messages

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
            messages.success(request, "Вы успешно зарегистрировались")
            return HttpResponseRedirect(reverse("authentication:login"))
    
    else:
        form = UserCreationForm()
        
    return render(request, "registration/register.html", {"form": form}) 


@login_required(login_url=reverse_lazy("authentication:login"))
def account_view(request):
    form_category = CategoryModelForm()
    form_bank_account = BankAccountModelForm()
    
    all_categories = Category.objects.filter(user=request.user)
    all_bank_accounts = BankAccount.objects.filter(user=request.user)
    
    context = {
        "form_category": form_category,
        "form_bank_account": form_bank_account,   
        
        "all_categories": all_categories,
        "all_bank_accounts": all_bank_accounts,     
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


@login_required(login_url=reverse_lazy("authentication:login"))
def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if category.user != request.user:
        return HttpResponseRedirect(reverse("authentication:account"))
    
    operations = Operation.objects.filter(category__id=category_id)
    print(operations)
    if (operations):
        message = ("Прежде чем удалить эту категорию, удалите все операции,\
                    в которых используется эта категория")
        messages.error(request, message)
    else:
        category.delete()
            
    return HttpResponseRedirect(reverse("authentication:account"))
    
    
@login_required(login_url=reverse_lazy("authentication:login"))
def delete_bank_account(request, bank_account_id):
    bank_account = get_object_or_404(BankAccount, pk=bank_account_id)
    if bank_account.user != request.user:
        return HttpResponseRedirect(reverse("authentication:account"))

    operations = Operation.objects.filter(bank_account__id=bank_account_id)
    if operations:
        message = "Прежде чем удалить этот счет, удалите все операции,\
                    в которых используется этот счет"
        messages.error(request, message)
        
    else:
        bank_account.delete()
        
    return HttpResponseRedirect(reverse("authentication:account"))


@login_required(login_url=reverse_lazy("authentication:login"))
def update_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    
    if request.method == "POST":
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            category.name = form.cleaned_data["name"]
            category.category_type = form.cleaned_data["category_type"]
            
            category.save()
            return HttpResponseRedirect(reverse("authentication:account"))
            
        
        
    form = CategoryModelForm(initial={"name": category.name, "category_type": category.category_type,})
    
    context = {
        "form": form,
    }

    return render(request, "registration/update_category.html", context=context)

@login_required(login_url=reverse_lazy("authentication:login"))
def update_bank_account(request, bank_account_id):
    bank_account = get_object_or_404(BankAccount, pk=bank_account_id)
    if request.method == "POST":
        form = BankAccountModelForm(request.POST)
        
        if form.is_valid():
            bank_account.name = form.cleaned_data["name"]
            
            bank_account.save()
            
            return HttpResponseRedirect(reverse("authentication:account"))
        
    form = BankAccountModelForm(initial={"name": bank_account.name, })
    context = {
        "form": form,
    }
    
    return render(request, "registration/update_bank_account.html", context=context)