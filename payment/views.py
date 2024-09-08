from rest_framework.viewsets import ModelViewSet
from helpers.timestampedmodel import TimeStampedModelMixin
from payment.models import Card, Coupon, Order, Cart
from payment.serializers import CardSerializer, CouponSerializer, OrderSerializer, CartSerializer
from rest_framework.authentication import TokenAuthentication
from stakeholders.permissions import IsOwner, IsEmployee, IsCustomer, IsSuperuser, HasOwnerGET, HasEmployeeGET, HasCustomerGET


class CardViewSet(ModelViewSet, TimeStampedModelMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsCustomer, HasOwnerGET, HasEmployeeGET]
    serializer_class = CardSerializer
    queryset = Card.objects.all()

class CouponViewSet(ModelViewSet, TimeStampedModelMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwner, IsEmployee, HasCustomerGET]
    serializer_class = CouponSerializer
    queryset = Coupon.objects.all()

class OrderViewSet(ModelViewSet, TimeStampedModelMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsCustomer, HasOwnerGET, HasEmployeeGET]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class CartViewSet(ModelViewSet, TimeStampedModelMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsCustomer, HasOwnerGET, HasEmployeeGET]
    serializer_class = CartSerializer
    queryset = Cart.objects.all()