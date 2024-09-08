from rest_framework.permissions import BasePermission

# guest permissions
class IsGuest(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_anonymous:
            return True
        return False
class HasGuestGET(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_anonymous:
            if request.method == "GET":
                return True
        return False
class HasGuestPOST(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_anonymous:
            if request.method == "POST":
                return True
        return False

# superuser permissions
class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and user.is_superuser and hasattr(user, "user_role", None) == "DEFAULT":
            return True
        return False

# owner permission
class IsOwner(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and getattr(user, "user_role", None) == "OWNER":
            return True
        return False

class HasOwnerGET(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and getattr(user, "user_role", None) == "OWNER":
            if request.method == "GET":
                return True
        return False
class HasOwnerPOST(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and getattr(user, "user_role", None) == "OWNER":
            if request.method == "POST":
                return True
        return False
class HasOwnerPUT(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and getattr(user, "user_role", None) == "OWNER":
            if request.method == "PUT":
                return True
        return False
class HasOwnerPATCH(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and getattr(user, "user_role", None) == "OWNER":
            if request.method == "PATCH":
                return True
        return False
class HasOwnerDELETE(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and getattr(user, "user_role", None) == "OWNER":
            if request.method == "DELETE":
                return True
        return False

# employee permissions
class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and getattr(user, "user_role", None) == "EMPLOYEE":
            return True
        return False

class HasEmployeeGET(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and getattr(user, "user_role", None) == "Employee":
            if request.method == "GET":
                return True
        return False
class HasEmployeePOST(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and getattr(user, "user_role", None) == "Employee":
            if request.method == "POST":
                return True
        return False
class HasEmployeePUT(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and getattr(user, "user_role", None) == "Employee":
            if request.method == "PUT":
                return True
        return False
class HasEmployeePATCH(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and getattr(user, "user_role", None) == "Employee":
            if request.method == "PATCH":
                return True
        return False
class HasEmployeeDELETE(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and getattr(user, "user_role", None) == "Employee":
            if request.method == "DELETE":
                return True
        return False

# customer permissions
class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and getattr(user, "user_role", None) == "CUSTOMER":
            return True
        return False

class HasCustomerGET(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        print(user.is_authenticated)
        if user and user.is_authenticated and getattr(user, "user_role", None) == "CUSTOMER":
            print(request.method)
            if request.method == "GET":
                return True
        return False
class HasCustomerPOST(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and getattr(user, "user_role", None) == "CUSTOMER":
            if request.method == "POST":
                return True
        return False
class HasCustomerPUT(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and getattr(user, "user_role", None) == "CUSTOMER":
            if request.method == "PUT":
                return True
        return False
class HasCustomerPATCH(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and getattr(user, "user_role", None) == "CUSTOMER":
            if request.method == "PATCH":
                return True
        return False
class HasCustomerDELETE(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and getattr(user, "user_role", None) == "CUSTOMER":
            if request.method == "DELETE":
                return True
        return False