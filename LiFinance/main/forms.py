from django import forms 

from django.forms import ModelForm

from .models import Operation
    
class ChequeModelForm(ModelForm):
    class Meta:
        model = Operation
        fields = '__all__'