from django.urls import path
from . import views

urlpatterns = [
    path("start/",views.index,name="index"),
    path("login/",views.login_form_user,name="login_form_user"),
    path("logins/",views.login_forms,name="login_forms"),
    path("signUp/",views.sign_up,name="sign_up"),
    path("<str:username>/expenseBlocks/",views.produceExpenseBlock,name="produceExpenseBlock"),
    path("<str:username>/expenseBlocks/<int:id>/",views.expenseShow,name="expenseShow"),
    path("logout/",views.logout_view,name="logout_view")

]