import factory
from django.contrib.auth.models import User
from .models import Account, Branch, Bank


class BankFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Bank

    name = factory.Faker('company')
    branch = factory.Faker('city')
    is_islamic = factory.Faker('boolean')

class BranchFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Branch

    branch_name = factory.Faker('city')
    bank = factory.SubFactory(BankFactory)

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')  #
    password = factory.PostGenerationMethodCall('set_password', 'password123')

class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    user = factory.SubFactory(UserFactory)
    branch = factory.SubFactory(BranchFactory)
    balance = factory.Faker('random_number', digits=3)
