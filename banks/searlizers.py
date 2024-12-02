from rest_framework import serializers
from .models import Bank, Account


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['name', 'is_islamic', 'branch']


class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['branch', 'balance']
