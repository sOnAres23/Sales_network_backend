from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsActiveUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_active:
            return True
        raise PermissionDenied("Ваш аккаунт неактивен. Обратитесь к администратору.")
