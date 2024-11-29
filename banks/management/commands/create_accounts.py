from django.core.management.base import  BaseCommand
from banks.models import Bank, Branch, Account
from django.contrib.auth.models import User
import logging


logger = logging.getLogger('__name__')


class Command(BaseCommand):
    help = 'Create accounts for all users in the HBL branch'

    def handle(self, *args, **options):
        try:
            hbl_branch = Branch.objects.get(id=1)
            users = User.objects.all()
            for user in users:
                account=Account.objects.create(
                    user=user,
                    branch=hbl_branch,
                    balance=0.0
                )
                logger.info(f'create account for {user.username} in branch{hbl_branch.branch_name}')

            self.stdout.write(self.style.SUCCESS(f"Successfully created accounts for {users.count()} users."))
        except Branch.DoesNotExist:
            logger.error("Branch with ID 1 (HBL Township) does not exist.")
            self.stdout.write(self.style.ERROR("Branch with ID 1 (HBL Township) does not exist."))
        except Exception as e:
            logger.error(f"Error creating accounts: {e}")
            self.stdout.write(self.style.ERROR(f"Error: {e}"))
