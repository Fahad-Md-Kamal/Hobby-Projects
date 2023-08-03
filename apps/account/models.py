from django.db import models
from django.contrib.auth import get_user_model
from .validators import validate_email_address


class UserManagementPermissons(models.Choices):
    CAN_ADD_USERS = "Can Add Users"
    CAN_REMOVE_USERS = "Can Remove Users"
    CAN_CHANGE_USERS = "Can Change Users"


class UsersProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='media/')
    contact = models.CharField(max_length=15)
    secondary_email = models.EmailField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        permissions = UserManagementPermissons.choices
        verbose_name_plural = "User Profile"
