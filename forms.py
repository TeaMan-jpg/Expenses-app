from django import forms


class CreateExpenseBlock(forms.Form):
    name = forms.CharField(max_length=200)
    current_Total_Expenses = forms.IntegerField()
    expense_Limit = forms.IntegerField()



class CreateExpense(forms.Form):
    text = forms.CharField(max_length=300)
    complete = forms.BooleanField()
    expenseAmount = forms.IntegerField()