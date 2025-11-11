from django import forms
from .models import BankAccount,Transaction,Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_type', 'balance']

class TransactionForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = ["account_number" ]  # user & account_number will be auto-generated
