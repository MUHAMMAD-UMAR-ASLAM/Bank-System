from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import BankListApiView, BankViewSet, BankListGenericView
from .views import BankListView, AccountListView, LoginView, UserAccountListView
from .views import (
    UpdateAccountBalanceView,
    DeleteAccountView,
    CreateAccountView,
    UserAccountApiView,
    CreateBankApiView,
    CreateAccountApiView,
    UpdateAccountApiView,
    AccountDetailAPIView,
    DeleteAccountApiView,
    AccountDetailUpdateDeleteAPIView,
)

urlpatterns = [
    path('banks/', BankListView.as_view(), name='bank-list'),
    path('accounts/', AccountListView.as_view(), name='account-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('user-accounts/', UserAccountListView.as_view(), name='user-account-list'),
    path('account/<int:account_id>/update_balance/', UpdateAccountBalanceView.as_view(), name='update_balance'),
    path('account/<int:account_id>/delete/', DeleteAccountView.as_view(), name='delete_account'),
    path('account/create/', CreateAccountView.as_view(), name='create_account'),
    path('banks/api/', BankListApiView.as_view(), name='api_view_banks'),
    path('banks/api/viewset/', BankViewSet.as_view({'get': 'list'}), name='viewset_banks'),
    path('banks/api/generic/', BankListGenericView.as_view(), name='generic_view_banks'),
    path('api/login/', obtain_auth_token, name='api_login'),
    path('accounts/api/', UserAccountApiView.as_view(), name='user_accounts'),
    path('banks/api/create/', CreateBankApiView.as_view(), name='create_bank'),
    path('accounts/api/create/', CreateAccountApiView.as_view(), name='create_account'),
    path('accounts/api/update/<int:pk>/', UpdateAccountApiView.as_view(), name='update_account'),
    path('accounts/api/detail/<int:pk>/', AccountDetailAPIView.as_view(), name='detail_account'),
    path('accounts/api/delete/<int:pk>/', DeleteAccountApiView.as_view(), name='delete_account'),
    path('accounts/api/detail-update-delete/<int:pk>/', AccountDetailUpdateDeleteAPIView.as_view(),
         name='detail_update_delete_account'),
]
