"""
Account admin
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""

from django.contrib import admin

# Local
from accounts.models import UserAuthentication


@admin.register(UserAuthentication)
class UserAuthenticationAdmin(admin.ModelAdmin):
    list_display = ('username', 'date', 'used_at')
