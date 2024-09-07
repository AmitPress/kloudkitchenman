from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stakeholders.views import OwnerViewSet, EmployeeViewSet, CustomerViewSet
router = DefaultRouter()
router.register("owner", OwnerViewSet, basename="owner")
router.register("employee", EmployeeViewSet)
router.register("customer", CustomerViewSet)

urlpatterns = [
    path(r"users/", include(router.urls))
]
