from rest_framework.viewsets import ModelViewSet
from helpers.timestampedmodel import TimeStampedModelMixin
from kitchen.models import Kitchen, Item, Category, Modifier, Menu
from kitchen.serializers import KitchenSerializer, ItemSerializer, CategorySerializer, ModifierSerializer, MenuSerializer
from rest_framework.authentication import TokenAuthentication
from stakeholders.permissions import IsOwner, IsEmployee, IsCustomer, IsSuperuser, HasOwnerGET, HasEmployeeGET, HasCustomerGET

# Create your views here.
class KitchenViewSet(ModelViewSet, TimeStampedModelMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwner]
    serializer_class = KitchenSerializer
    queryset = Kitchen.objects.all()

class ItemViewSet(ModelViewSet, TimeStampedModelMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsOwner | IsEmployee | HasCustomerGET,)
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class CategoryViewSet(ModelViewSet, TimeStampedModelMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsOwner | IsEmployee | HasCustomerGET,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ModifierViewSet(ModelViewSet, TimeStampedModelMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsOwner | IsEmployee | HasCustomerGET,)
    serializer_class = ModifierSerializer
    queryset = Modifier.objects.all()

class MenuViewSet(ModelViewSet, TimeStampedModelMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsOwner | IsEmployee | HasCustomerGET,)
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()