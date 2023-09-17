import os
from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth import get_user_model

import random
from config.settings import BASE_DIR


user = get_user_model()


class Command(BaseCommand):
    help = "Generate Initial Superuser"

    def handle(self, *args, **options):
        """
        Generate initial superuser `nimbus-admin` if there is none.

        Find the initial user's password into the project's root directory's `.password`
        """
        chars = "ABCDEFGHIJKLMNOPQURSTabcdefghijklmnopqrstuvwxyz1234567890#@$%!"
        random_chars = random.sample(chars, 15)
        random_string = ''.join(random_chars)
        user_data, is_created = user.objects.get_or_create(username="nimbus-admin", is_superuser=True, is_active=True, is_staff=True)
        if is_created:
            user_data.set_password(random_string)
            user_data.save()
            with open(f"{BASE_DIR}/.password", "w") as file:
                file.write(random_string)
                print(random_string)
            