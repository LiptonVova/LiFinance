from django import forms  

from main.models import Category, BankAccount

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name", "category_type", )
        
        
class BankAccountModelForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = ("name", )