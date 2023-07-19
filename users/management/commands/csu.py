from django.core.management import BaseCommand
from users.models import User
import os


PASSWORD = os.getenv('PASS_EMAIL')

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='89601383333e@gmail.com',
            first_name='Admin',
            last_name='SuperUser',
            is_staff=True,
            is_superuser=True
        )

        user.set_password(PASSWORD)
        user.save()
