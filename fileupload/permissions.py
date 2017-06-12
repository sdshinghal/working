from rest_framework import permissions


class IsGroupOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only owners of an object
    """
    message = "You must have permission to upload a file"

    def has_permission(self, request, view):

        return request.user.groups == "ReadandWrite"

