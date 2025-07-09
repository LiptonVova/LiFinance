from django.shortcuts import render
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.forms import modelform_factory

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Category, BankAccount, Operation
from .forms import ChequeModelForm, ContentForm

@login_required(login_url=reverse_lazy("authentication:login"))
def index(request):
    categories = Category.objects.filter(user=request.user)
    categories_expense = dict()
    categories_income = dict()

    for category in categories:
        if category.category_type == "IN":
            # сумма доходов только за данную категорию
            amount = Operation.objects.filter(category=category).aggregate(Sum('sum')) 
            categories_income[category.name] = amount["sum__sum"]
        
        elif category.category_type == "EX":
            # сумма доходов только за данную категорию
            amount = Operation.objects.filter(category=category).aggregate(Sum('sum'))
            categories_expense[category.name] = amount["sum__sum"]

    bank_accounts = BankAccount.objects.filter(user=request.user)   
    bank_account_expense = dict()
    bank_account_income = dict()
    
    for account in bank_accounts:
        amount_expense = (
                Operation.objects.filter(bank_account=account) & Operation.objects.filter(operation_type="EX")
            ).aggregate(Sum('sum'))
        amount_income = (
            Operation.objects.filter(bank_account=account) & Operation.objects.filter(operation_type="IN")
            ).aggregate(Sum('sum'))
        if (amount_expense["sum__sum"] is not None):
            bank_account_expense[account.name] = amount_expense["sum__sum"]
        if (amount_income["sum__sum"] is not None):
            bank_account_income[account.name] = amount_income["sum__sum"]
        
    last_cheques = Operation.objects.filter(user=request.user)[:5]
    
    context = {
        "categories_expense": categories_expense,
        "categories_income": categories_income,
        
        "bank_account_expense": bank_account_expense,
        "bank_account_income": bank_account_income,
        
        "last_cheques": last_cheques,   
    }
    
    return render(request, 'main/index.html', context=context)

@login_required(login_url=reverse_lazy('authentication:login'))
def add_cheque(request):
    if request.method == "POST":
        form = ChequeModelForm(request.user, request.POST)
        
        if form.is_valid():
            op = Operation()
            op.sum = form.cleaned_data["sum"]
            op.content = form.cleaned_data["content"]
            op.date = form.cleaned_data["date"]
            op.operation_type = form.cleaned_data["operation_type"]
            op.category = form.cleaned_data["category"]
            op.bank_account = form.cleaned_data["bank_account"]
            op.user = request.user
            
            op.save()
                        
            return HttpResponseRedirect(reverse('main:index'))
    
    else:        
        form = ChequeModelForm(user=request.user)
        form_content = ContentForm()
                
    context = {
        "form": form,
        "form_content": form_content,
    }
                
    return render(request, 'main/add_cheque.html', context=context)


def add_content(request):
    form = ContentForm(request.GET)
    