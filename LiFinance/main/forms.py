from django import forms 

from .models import Operation, Category, BankAccount
    
    
class ChequeModelForm(forms.ModelForm):    
    def __init__(self, user, *args, **kwargs):
        super(ChequeModelForm, self).__init__(*args, **kwargs)
        self.fields["category"] = forms.ModelChoiceField(queryset=Category.objects.filter(user=user))
        self.fields["bank_account"] = forms.ModelChoiceField(queryset=BankAccount.objects.filter(user=user))

            
    class Meta:
        model = Operation
        fields = ("sum", "content", "date", "operation_type", 
                  "category", "bank_account", )
        # fields = '__all__'