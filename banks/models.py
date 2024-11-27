from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=255)
    branch = models.CharField(max_length=100)
    is_islamic = models.BooleanField(default=False)

    def __str__(self):
        return  self.name


class Account(models.Model):
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"Account of {self.user.name} at {self.bank.name}"



