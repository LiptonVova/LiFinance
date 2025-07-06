from django.db import models

from django.utils import timezone

type_choices = {
    "IN": "Доход",
    "EX": "Расход",
    }


class Category(models.Model):
    name = models.CharField(max_length=50)
    category_type = models.CharField(choices=type_choices)
    
    def __str__(self):
        return f"{self.name}"
    
    
class BankAccount(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"


class Operation(models.Model):
    
    sum = models.IntegerField()
    content = models.CharField(max_length=500)
    date = models.DateField(default=timezone.now())
    operation_type = models.CharField(choices=type_choices)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"<Operation with sum {self.sum}: category - {self.category.name}, bank account - {self.bank_account.name}>"
