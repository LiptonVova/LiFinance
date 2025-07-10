from django.shortcuts import render
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.shortcuts import get_object_or_404

import json

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
            if amount["sum__sum"] is not None:
                categories_income[category.name] = amount["sum__sum"]
        
        elif category.category_type == "EX":
            # сумма доходов только за данную категорию
            amount = Operation.objects.filter(category=category).aggregate(Sum('sum'))
            if (amount["sum__sum"] is not None):
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
            transaction = form.save(commit=False)

            transaction.user = request.user
            
            items_data = request.POST.get('items_data', '[]')
            try:
                transaction.content = json.loads(items_data)    
            except json.JSONDecodeError:
                transaction.content = []
                
                       
            transaction.save()
            return HttpResponseRedirect(reverse('main:index'))
    
    else:        
        form = ChequeModelForm(user=request.user)

    context = {
        "edit_mode": False,
        "form": form,
    }
    return render(request, 'main/cheque.html', context=context)


@login_required(login_url=reverse_lazy('authentication:login'))
def delete_cheque(request, cheque_id):
    cheque = Operation.objects.filter(pk=cheque_id)
    if cheque is not None:
        cheque.delete()
    return HttpResponseRedirect(reverse('main:index'))


@login_required(login_url=reverse_lazy('authentication:login'))
def update_cheque(request, cheque_id):
    cheque = get_object_or_404(Operation, pk=cheque_id)
    if cheque is None or cheque.user != request.user:
        return HttpResponseRedirect(reverse('main:index'))
    
    
    if request.method == 'POST':
        form = ChequeModelForm(request.user, request.POST)
        if form.is_valid():
            cheque.sum = form.cleaned_data["sum"]
            cheque.date = form.cleaned_data["date"]
            cheque.operation_type = form.cleaned_data["operation_type"]
            cheque.category = form.cleaned_data["category"]
            cheque.bank_account = form.cleaned_data["bank_account"]
             
            items_data = request.POST.get('items_data', '[]')
            try:
                cheque.content = json.loads(items_data)
            except json.JSONDecodeError:
                cheque.content = []
                
            cheque.save()
            return HttpResponseRedirect(reverse('main:index'))
                        
                        
    form = ChequeModelForm(user=request.user)
    form.initial = {
        "sum": cheque.sum,
        "date": cheque.date,
        "operation_type": cheque.operation_type,
        "category": cheque.category,
        "bank_account": cheque.bank_account,
    }
    
    context = {
        "edit_mode": True,
        "cheque_items_json": json.dumps(cheque.content),
        "form": form,
    }

    return render(request, "main/cheque.html", context=context)