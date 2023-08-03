from django.db.models import Manager
from django.contrib.auth import get_user_model


class UsersProfileManager(Manager):

    def change_email(self, user_id: int, email: str):
        db_user = get_user_model().objects.filter(id=user_id)
        if db_user.exists():
            db_user.update(email=email)
            return True
        return False

