from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, \
    RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from .models import Bank, Account
from .searlizers import BankSerializer, AccountSerializer


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
        accounts = request.user.accounts.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)


class CreateBankApiView(CreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class CreateAccountApiView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UpdateAccountApiView(UpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.accounts.all()


class AccountDetailAPIView(RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.accounts.all()


class DeleteAccountApiView(DestroyAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.accounts.all()


class AccountDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        return self.request.user.accounts.all()
