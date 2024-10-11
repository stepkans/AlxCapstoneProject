# posts/permissions.py
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only authors to edit or delete their own posts.
    Everyone can view the list and detail of posts.
    """
    
    def has_permission(self, request, view):
        # Allow all users (authenticated or not) to view the post list and detail.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow only authenticated users to create posts.
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow read-only permissions for everyone.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only allow the author of the post to edit or delete it.
        return obj.author == request.user