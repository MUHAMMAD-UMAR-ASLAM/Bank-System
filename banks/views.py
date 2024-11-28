from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DjangoLoginView
from .models import Bank, Account

class BankListView(ListView):
    model = Bank
    template_name = 'bank_list.html'
    context_object_name = 'banks'


class AccountListView(LoginRequiredMixin,ListView):
    model = Account
    template_name = 'account_list.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        self.request.user.accounts.all()


class LoginView(DjangoLoginView):
    template_name = 'login.html'


class UserAccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = 'user_account_list.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        return self.request.user.accounts.all()
