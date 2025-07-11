from django import forms 

from django.utils import timezone

class RangeDateForm(forms.Form):
    start_date = forms.DateField(initial=timezone.now(), widget=forms.DateInput(attrs={"type": "date", }))
    end_date = forms.DateField(initial=timezone.now(), widget=forms.DateInput(attrs={"type": "date", }))