from django.contrib.auth.models import User
from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=255)
    branch = models.CharField(max_length=100)
    is_islamic = models.BooleanField(default=False)

    def __str__(self):
        return  self.name


class Branch(models.Model):
    branch_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='branches')

    def __str__(self):
        return f"{self.branch_name} at {self.bank.name}"


class Account(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='accounts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')

    def __str__(self):
        return f"Account of {self.user.username} at {self.branch.branch_name}"
