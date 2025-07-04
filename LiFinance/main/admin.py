from django.contrib import admin

from .models import Category, BankAccount, Operation

admin.site.register(Category)
admin.site.register(BankAccount)

@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'sum', 'category', 'content', 'date', 'bank_account',
    )
    
    list_filter = ('category',)
    
    fieldsets = (
        ("Основная информация", {
            'fields': ("content", )
        } ),
        ("Служебная информация", {
            'fields': ("sum", "category", "bank_account", "date", )
        }),
    )
