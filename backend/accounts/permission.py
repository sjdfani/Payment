from rest_framework.permissions import BasePermission


class IsAccount(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user and request.user.is_superuser or obj.user == request.user
        )


class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_superuser
        )
