from django import  forms
from django.db.models import Q

from .models import Account, Branch

class AccountBalanceUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['balance']


class NewAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['branch', 'balance']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['branch'].queryset = Branch.objects.filter(
                ~Q(accounts__user=user)
            )
