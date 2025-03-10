from django.contrib import admin
from .models import CustomUser, UserProfile, Chat
from django.contrib.auth.admin import UserAdmin

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profiles'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Chat)