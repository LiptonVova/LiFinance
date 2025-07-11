from django.contrib import admin

from .models import Category, BankAccount, Operation

admin.site.register(Category)
admin.site.register(BankAccount)

@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'operation_type', 'sum', 'category', 'content', 'date', 'bank_account',
    )
    
    list_filter = ('category',)
    
    fieldsets = (
        ("Основная информация", {
            'fields': ("content", )
        } ),
        ("Служебная информация", {
            'fields': ("operation_type","sum", "category", "bank_account", "date", )
        }),
    )
