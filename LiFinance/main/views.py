from django.shortcuts import render
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.forms import modelform_factory

from .models import Category, BankAccount, Operation
from .forms import ChequeModelForm

def index(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    
    categories = Category.objects.all()
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

    bank_accounts = BankAccount.objects.all()    
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
        
    last_cheques = Operation.objects.filter()[:5]
    
    context = {
        "categories_expense": categories_expense,
        "categories_income": categories_income,
        
        "bank_account_expense": bank_account_expense,
        "bank_account_income": bank_account_income,
        
        "last_cheques": last_cheques,   
        
        "num_visits": num_visits,    
    }
    
    return render(request, 'index.html', context=context)


def add_cheque(request):
    if request.method == "POST":
        form = ChequeModelForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index'))
    
    else:
        form = ChequeModelForm()
        # form = modelform_factory(Operation, fields="__all__") # тоже самое, что и предыдущее, но короче
        
    return render(request, 'add_cheque.html', {"form": form})