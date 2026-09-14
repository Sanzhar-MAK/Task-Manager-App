from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.author
