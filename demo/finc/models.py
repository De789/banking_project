import uuid
from django.db import models
from django.contrib.auth.models import User
import uuid 
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
 

def generate_account_number():
    """Generate a short unique account number."""
    return str(uuid.uuid4().int)[:12]  # 12-digit unique number


class Account(models.Model):
    # Link each account to a user
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Unique account number
    account_number = models.CharField(
        max_length=20,
        unique=True,
        default=generate_account_number
    )

    ACCOUNT_TYPES = (
        ('SAVINGS', 'Savings Account'),
        ('CURRENT', 'Current Account'),
    )

    account_type = models.CharField(
        max_length=20,
        choices=ACCOUNT_TYPES,
        default='SAVINGS'   # default to avoid migration issues
    )

    # Balance with default 0
    # balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    # Track creation time
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.account_number}"

class BankAccount(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True) 
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.account_number}"

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transactions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=[("Deposit", "Deposit"), ("Withdraw", "Withdraw")])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account.account_number} - {self.transaction_type} - {self.amount}"
 
