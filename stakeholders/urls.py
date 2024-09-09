from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stakeholders.views import OwnerViewSet, EmployeeViewSet, CustomerViewSet, UserSigninViewSet, CustomerSignupViewSet
router = DefaultRouter()
router.register("owner", OwnerViewSet, basename="owner")
router.register("employee", EmployeeViewSet, basename="employee")
router.register("customer", CustomerViewSet, basename="customer")
router.register("signin", UserSigninViewSet, basename="signin")
router.register("customer-signup", CustomerSignupViewSet, basename="signup")


urlpatterns = [
    path(r"users/", include(router.urls))
]
