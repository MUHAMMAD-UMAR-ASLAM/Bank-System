from django.contrib import admin
from .models import Bank, Account, Branch
# Register your models here.

admin.site.register(Bank)
admin.site.register(Account)
admin.site.register(Branch)
