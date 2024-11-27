from django.urls import path
from .views import BankListView, AccountListView, LoginView, UserAccountListView

urlpatterns = [
    path('banks/', BankListView.as_view(), name='bank-list'),
    path('accounts/', AccountListView.as_view(), name='account-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('user-accounts/', UserAccountListView.as_view(), name='user-account-list'),
]
