from decimal import Decimal
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Account
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import *
import random
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,"home.html")

@csrf_exempt
def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            Account.objects.create(user=user)
    else:
        form=UserCreationForm()
    return render(request,"register.html",{'fomr':form})

def login(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

def open_account(request):
    if request.method=="POST":
        form=AccountForm(request.POST)
        if form.is_valid():
            account=form.save(commit=False)
            account.user=request.user
            account.account_number = str(random.randint(1000000000, 9999999999))
            account.save()
            return redirect('dashboard')
    else:
        form=AccountForm()
    return render(request,'open_account.html',{'form':form})

 
def deposit(request):
    if request.method == "POST":
        account_id = request.POST.get('account_id')
        amount = request.POST.get('amount')

        try:
            account = Account.objects.get(id=account_id, user=request.user)
            account.balance += Decimal(amount)  # ✅ Convert to Decimal
            account.save()
            messages.success(request, "Deposit successful!")
            return redirect('dashboard')
        except Account.DoesNotExist:
            messages.error(request, "Account not found.")
        except Exception as e:
            messages.error(request, f"Error: {e}")

    accounts = Account.objects.filter(user=request.user)
    return render(request, 'deposit.html', {'accounts': accounts})

def withdraw(request):
    if request.method == "POST":
        account_id = request.POST.get('account_id')
        amount = request.POST.get('amount')

        try:
            account = Account.objects.get(id=account_id, user=request.user)
            amount_decimal = Decimal(amount)

            if account.balance >= amount_decimal:
                account.balance -= amount_decimal
                account.save()

                # ✅ Record transaction
                Transaction.objects.create(account=account, transaction_type='WITHDRAW', amount=amount_decimal)

                messages.success(request, "Withdrawal successful!")
            else:
                messages.error(request, "Insufficient balance!")

            return redirect('dashboard')

        except Account.DoesNotExist:
            messages.error(request, "Account not found.")
        except Exception as e:
            messages.error(request, f"Error: {e}")

    accounts = Account.objects.filter(user=request.user)
    return render(request, 'withdraw.html', {'accounts': accounts})

def dashboard(request):
    accounts = Account.objects.filter(user=request.user)
    transactions = Transaction.objects.filter(account__in=accounts).order_by('-timestamp')

    return render(request, 'dashboard.html', {'accounts': accounts, 'transactions': transactions})

# def deposit(request):
#     # account = Account.objects.get(user=request.user)
#     if request.method == 'POST':
#         form = TransactionForm(request.POST)
#         if form.is_valid():
#             account.balance += form.cleaned_data['amount']
#             account.save()
#             return redirect('dashboard')
#     else:
#         form = TransactionForm()
#     return render(request, 'transaction.html', {'form': form, 'title': 'Deposit'})

def withdraw(request):
    account = Account.objects.get(user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            account.balance -= form.cleaned_data['amount']
            account.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    return render(request, 'transaction.html', {'form': form, 'title': 'Withdraw'})

 

 



   