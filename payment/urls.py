from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payment.views import CardViewSet, CartViewSet, CouponViewSet, OrderViewSet

router = DefaultRouter()

router.register("cards", CardViewSet, basename="cards")
router.register("carts", CartViewSet, basename="carts")
router.register("coupons", CouponViewSet, basename="coupons")
router.register("orders", OrderViewSet, basename="orders")

urlpatterns = [
    path(r"payment/", include(router.urls))
]