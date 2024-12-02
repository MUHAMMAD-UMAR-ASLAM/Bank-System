from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import ListView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from .forms import AccountBalanceUpdateForm, NewAccountForm
from .models import Bank, Account
from .searlizers import BankSerializer, AccountSerializers


class BankListView(ListView):
    model = Bank
    template_name = 'bank_list.html'
    context_object_name = 'banks'

    @method_decorator(cache_page(10))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AccountListView(LoginRequiredMixin, ListView):
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


class UpdateAccountBalanceView(LoginRequiredMixin, View):
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


class BankListApiView(APIView):
    def get(self, request):
        banks = Bank.objects.all()
        data = [{'id': bank.id, 'name': bank.name, 'is_islamic': bank.is_islamic} for bank in banks]
        return Response(data)


class BankViewSet(ViewSet):
    def list(self, request):
        banks = Bank.objects.all()
        data = [{'id': bank.id, 'name': bank.name, 'is_islamic': bank.is_islamic} for bank in banks]
        return Response(data)


class BankListGenericView(ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class UserAccountApiView(APIView):
    def get(self, request):
        accounts = Account.objects.filter(user=request.user)
        serializer = AccountSerializers(accounts, many=True)
        return Response(serializer.data)


class CreateBankApiView(CreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class CreateAccountApiView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UpdateAccountApiView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers


class AccountDetailAPIView(RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers


class DeleteAccountApiView(DestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers


class AccountDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers
