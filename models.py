from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ExpenseBlock(models.Model):

    name = models.CharField(max_length=200)
    expenseLimit = models.IntegerField(default=0)
    currentTotalExpense = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="expense_block")



    def __str__(self):
        return self.name
    

class Expenses(models.Model):
    expenseList = models.ForeignKey(ExpenseBlock,on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    expenseAmount = models.IntegerField(default=0)
    datetime = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.text
