from django.db import models

from django.utils import timezone

# class User(models.Model):
#     login = models.CharField(max_length=50, unique=True)
#     hash_password = models.


class Category(models.Model):
    name = models.CharField(max_length=50)
    type_choices = {
        "IN": "Доход",
        "EX": "Расход",
        }
    category_type = models.CharField(choices=type_choices)
    
    def __str__(self):
        return f"<Category {self.name}>"
    
    
class BankAccount(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"<BankAccount {self.name}>"


class Operation(models.Model):
    
    sum = models.IntegerField()
    content = models.TextField()
    date = models.DateField(default=timezone.now())
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"<Operation with sum {self.sum}: category - {self.category}, bank account - {self.bank_account}>"
