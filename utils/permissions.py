"""
Custom permissions
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""


from rest_framework import permissions


class IsAuthenticatedOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated