from django.contrib import admin
from .models import UsersProfile




@admin.register(UsersProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "profile_owner", "contact"]
    
    @admin.display(description="Profile Owner")
    def profile_owner(self, obj):
        return obj.user.username
    