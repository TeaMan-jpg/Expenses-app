from django.contrib import admin
from .models import ExpenseBlock,Expenses
# Register your models here.
admin.site.register(Expenses)
admin.site.register(ExpenseBlock)