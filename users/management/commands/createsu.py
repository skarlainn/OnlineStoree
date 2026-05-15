from django.contrib.auth.middleware import get_user
from django.core.management.base import BaseCommand

from users.models import User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(email="admin@mail.com")
        user.set_password("admin123")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
