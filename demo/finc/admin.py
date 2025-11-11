from django.contrib import admin
from .models import Account,BankAccount,Transaction

# Register your models here.
admin.site.register(Account)
admin.site.register(BankAccount)
admin.site.register(Transaction)
