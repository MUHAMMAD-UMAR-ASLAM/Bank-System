from django.urls import path
from .views import BankListView, AccountListView, LoginView, UserAccountListView
from .views import UpdateAccountBalanceView,DeleteAccountView,CreateAccountView

urlpatterns = [
    path('banks/', BankListView.as_view(), name='bank-list'),
    path('accounts/', AccountListView.as_view(), name='account-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('user-accounts/', UserAccountListView.as_view(), name='user-account-list'),
    path('account/<int:account_id>/update_balance/', UpdateAccountBalanceView.as_view(), name='update_balance'),
    path('account/<int:account_id>/delete/', DeleteAccountView.as_view(), name='delete_account'),
    path('account/create/', CreateAccountView.as_view(), name='create_account'),
]
