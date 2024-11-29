from django.test import TestCase
from django.urls import reverse
from .factories import AccountFactory, UserFactory, BranchFactory, BankFactory


class UserAccountListViewTest(TestCase):
    def setUp(self):
        self.bank = BankFactory(name="HBL", branch="Township", is_islamic=True)
        self.branch = BranchFactory(branch_name='Test Bank', bank=self.bank)
        self.user = UserFactory(username='testuser')
        self.account_1 = AccountFactory(user=self.user, branch=self.branch, balance=100)
        self.account_2 = AccountFactory(user=self.user, branch=self.branch, balance=200)
        self.client = self.client_class()

    def test_account_list_view(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('user-account-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['accounts']), 2)
        self.assertEqual(response.context['accounts'][0], self.account_1)
        self.assertEqual(response.context['accounts'][1], self.account_2)
        self.assertTemplateUsed(response, 'user_account_list.html')



