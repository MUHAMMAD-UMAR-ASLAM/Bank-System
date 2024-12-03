from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .api_views import (
    BankListAPIView,
    BankViewSet,
    BankListGenericView,
    UserAccountAPIView,
    CreateBankAPIView,
    CreateAccountAPIView,
    UpdateAccountAPIView,
    AccountDetailAPIView,
    DeleteAccountAPIView,
    AccountDetailUpdateDeleteAPIView,
)

urlpatterns = [
    # Bank APIs
    path('banks', BankListAPIView.as_view(), name='api_view_banks'),
    path('api/login/', obtain_auth_token, name='api_login'),
    path('banks/api/viewset/', BankViewSet.as_view({'get': 'list'}), name='viewset_banks'),
    path('banks/api/generic/', BankListGenericView.as_view(), name='generic_view_banks'),
    path('banks/api/create/', CreateBankAPIView.as_view(), name='create_bank'),
    # Account APIs
    path('accounts/', CreateAccountAPIView.as_view(), name='create_account'),
    path('accounts/api/', UserAccountAPIView.as_view(), name='user_accounts'),
    path('accounts/api/update/<int:pk>/', UpdateAccountAPIView.as_view(), name='update_account'),
    path('accounts/api/detail/<int:pk>/', AccountDetailAPIView.as_view(), name='detail_account'),
    path('accounts/api/delete/<int:pk>/', DeleteAccountAPIView.as_view(), name='delete_account'),
    path('accounts/<int:pk>/', AccountDetailUpdateDeleteAPIView.as_view(),
         name='detail_update_delete_account'),
]
