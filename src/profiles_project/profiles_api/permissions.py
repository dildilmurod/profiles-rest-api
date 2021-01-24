from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allows edit own profile"""
    def has_object_permission(self, request, view, obj):
        """Check user is editing own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id