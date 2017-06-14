from rest_framework import permissions
from django.contrib.auth.models import Group



class IsGroupOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only owners of an object
    """
    message = "You must have permission to upload a file"

    def has_permission(self, request, view):
        allowed = False
        group = Group.objects.get(name='ReadandWrite')
        user_groups = request.user.groups.all()
        if group in user_groups:
            allowed = True
        elif request.user.is_staff:
            allowed = True
        return allowed

