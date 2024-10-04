from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import CreateExpenseBlock,CreateExpense
from .models import ExpenseBlock,Expenses
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
# Create your views here.

def index(res):

    return HttpResponse("<h1>Hello</h1>")


def login_user(req):

    return render(req,"authenticate/login.html",{})


def login_form_user(res):
    
    form = CreateExpenseBlock()

    if (res.method == "POST"):

        form = CreateExpenseBlock(res.POST)

        if (form.is_valid()):

            expenseBlockName = form.cleaned_data["name"]
            totalExpenses = form.cleaned_data["current_Total_Expenses"]
            expenseLimit = form.cleaned_data["expense_Limit"]

            e = ExpenseBlock(name=expenseBlockName,currentTotalExpense=totalExpenses,expenseLimit=expenseLimit)

            e.save()
         
        else:

            form = CreateExpenseBlock()

    return render(res,"expenses/authentication.html",{"form":form})


def login_forms(req):


    if req.method == "POST":

        username = req.POST['username']
        password = req.POST['password']
     
        user = authenticate(username=username,password=password)

        if user is not None:
            messages.success(req,"Login successful!")
            login(req,user)
            return redirect(f"/expenses/{req.user.username}/expenseBlocks/")
            
        else:
            messages.error(req,"Login Failed! User not Found.")

        

        
    return render(req,"authenticate/authentication.html",{"username":"none","password":"none"})


def sign_up(req):

    if req.method == "POST":

        username = req.POST['username']
        password = req.POST['password']
        email = req.POST['email']

        if (username and password and email):
            user = User.objects.create_user(username=username,email=email,password=password)
        
            contenttype = ContentType.objects.get_for_model(ExpenseBlock)

            post_permission = Permission.objects.filter(content_type=contenttype)

            for perm in post_permission:
                user.user_permissions.add(perm)

        
            user.save()
            return redirect(f"/expenses/{username}/expenseBlocks/")

    return render(req,"expenses/signUp.html",{})


def produceExpenseBlock(req,username):

    user = get_object_or_404(User, username=username)

    expenseBlocks = ExpenseBlock.objects.filter(user=user)
    

    form = CreateExpenseBlock()

    if (req.user.is_authenticated):
        if (req.method == "POST"):

            form = CreateExpenseBlock(req.POST)

            if (form.is_valid()):

                name = form.cleaned_data['name']
                currentTotalExpense = form.cleaned_data['current_Total_Expenses']
                expenseLimit = form.cleaned_data['expense_Limit']

                e = ExpenseBlock(name=name,currentTotalExpense=currentTotalExpense,expenseLimit=expenseLimit,user=req.user)
                e.save()
            else:
                form = CreateExpenseBlock()

            

    return render(req,"expenses/expenseFile.html",{"expenses":expenseBlocks,"form":form})



def expenseShow(res, id,username):
    # Fetch the expense based on the 'id'
    
    user = get_object_or_404(User, username=username)




    expense = get_object_or_404(ExpenseBlock,user=user, id=id)
    form = CreateExpense()
    if res.method == "POST":
       
        form = CreateExpense(res.POST)

        if (form.is_valid()):
            print("bgbhrt")
            text = form.cleaned_data['text']
            complete = form.cleaned_data['complete']
            expenseAmount = form.cleaned_data['expenseAmount']

            print(text)
            print(complete)
            print(expenseAmount)
            print(expense.currentTotalExpense)

            if ((expense.currentTotalExpense + int(expenseAmount)) > expense.expenseLimit):

                messages.error(res,"TotalExpense Filled")
            else:

                expense.expenses_set.create(

                    text=text,
                    complete=complete,
                    expenseAmount=expenseAmount
                )
              
                expense.currentTotalExpense += int(expenseAmount)
                expense.save()

        else:
            form = CreateExpense()



   
    print(expense)
    return render(res, 'expenses/expenseShowcase.html', {'expense': expense,"form":form,"username":username})


def logout_view(req):
    if (req.method == "POST"):
        logout(req)
        return redirect("/expenses/logins/")
    
    return render(req,"expenses/logout.html",{})