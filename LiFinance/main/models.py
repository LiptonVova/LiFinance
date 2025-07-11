from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

type_choices = {
    "IN": "Доход",
    "EX": "Расход",
    }


class Category(models.Model):
    name = models.CharField(max_length=50)
    category_type = models.CharField(choices=type_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    def __str__(self):
        return f"{self.name}"
    
    def get_category_type(self):
        return type_choices[self.category_type]
    
    
class BankAccount(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}"


class Operation(models.Model):
    name = models.CharField(max_length=100)
    sum = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    content = models.JSONField(default=list, blank=True, null=True)
    date = models.DateField(default=timezone.now())
    operation_type = models.CharField(choices=type_choices)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"<Operation with sum {self.sum}: category - {self.category.name}, bank account - {self.bank_account.name}>"


    def get_operation_type(self):
        return type_choices[self.operation_type]