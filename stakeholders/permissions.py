from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and hasattr(user, "user_role", None) == "OWNER":
            return True
        return False

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and hasattr(user, "user_role", None) == "EMPLOYEE":
            return True
        return False
class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and hasattr(user, "user_role", None) == "CUSTOMER":
            return True
        return False