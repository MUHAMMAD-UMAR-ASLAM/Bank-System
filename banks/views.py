from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DjangoLoginView
from .forms import AccountBalanceUpdateForm, NewAccountForm
from .models import Bank, Account
from  django.views import View
from django.shortcuts import get_object_or_404, redirect


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


class UpdateAccountBalanceView(LoginRequiredMixin,View):
    def get(self, request, account_id):
        account = get_object_or_404(Account, id=account_id, user=request.user)
        form = AccountBalanceUpdateForm(instance=account)
        return render(request, 'update_balance.html', {'form': form, 'account': account})


    def post(self, request, account_id):
        account = get_object_or_404(Account, id=account_id, user=request.user)
        form = AccountBalanceUpdateForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('user-account-list')
        return render(request, 'update_balance.html', {'form': form, 'account': account})


class DeleteAccountView(LoginRequiredMixin, View):
    def get(self, request, account_id):
        account = get_object_or_404(Account, id=account_id, user=request.user)
        account.delete()
        return redirect('user-account-list')


class CreateAccountView(LoginRequiredMixin, View):
    def get(self, request):
        form = NewAccountForm(user=request.user)
        return render(request, 'create_account.html', {'form': form})

    def post(self, request):
        form = NewAccountForm(request.POST, user=request.user)
        if form.is_valid():
            new_account = form.save(commit=False)
            new_account.user = request.user
            new_account.save()
            return redirect('user-account-list')
        return render(request, 'create_account.html', {'form': form})
