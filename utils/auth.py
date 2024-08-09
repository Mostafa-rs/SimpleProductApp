"""
auth utility functions
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""

from rest_framework_simplejwt.tokens import RefreshToken


def get_auth_token(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
