from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allows edit own profile"""
    def has_object_permission(self, request, view, obj):
        """Check user is editing own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    """Allow users to update own status"""

    def has_object_permission(self, request, view, obj):
        """Checks user is trying update own status"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
