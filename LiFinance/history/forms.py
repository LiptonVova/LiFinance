from django import forms 

from django.utils import timezone

class RangeDateForm(forms.Form):
    start_date = forms.DateField(initial=timezone.now(), widget=forms.DateInput(attrs={"type": "date", }))
    end_date = forms.DateField(initial=timezone.now(), widget=forms.DateInput(attrs={"type": "date", }))
     
    # def clean__start_date(self):
    #     data = self.cleaned_data.get('start_date')
    #     return data
    
    # def clean__end_date(self):
    #     data = self.cleaned_data.get('end_date')
    #     return data
    
    
    def clean_start_date(self):
        data = self.cleaned_data["start_date"]
        return data

    def clean_end_date(self):
        data = self.cleaned_data["end_date"]
        return data