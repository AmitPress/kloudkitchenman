from django.urls import path, include
from rest_framework.routers import DefaultRouter
from kitchen.views import KitchenViewSet, ItemViewSet, CategoryViewSet, ModifierViewSet, MenuViewSet
router = DefaultRouter()

router.register("kitchens", KitchenViewSet, basename="kitchens")
router.register("items", ItemViewSet, basename="items")
router.register("categories", CategoryViewSet, basename="categories")
router.register("modifiers", ModifierViewSet, basename="modifiers")
router.register("menus", MenuViewSet, basename="menus")

urlpatterns = [
    path(r"kitchen/", include(router.urls))
]