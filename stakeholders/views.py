from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from stakeholders.permissions import IsOwner, IsEmployee, IsCustomer
from stakeholders.serializers import OwnerSerializer, EmployeeSerializer, CustomerSerializer
from stakeholders.models import Owner, Employee, Customer

# viewset

class OwnerViewSet(ModelViewSet):
    # authentication_classes  = [TokenAuthentication]
    # permission_classes      = [IsOwner]
    serializer_class        = OwnerSerializer
    queryset                = Owner.objects.all()


class EmployeeViewSet(ModelViewSet):
    # authentication_classes  = [TokenAuthentication]
    # permission_classes      = [IsEmployee]
    serializer_class        = EmployeeSerializer
    queryset                = Employee.objects.all()


class CustomerViewSet(ModelViewSet):
    # authentication_classes  = [TokenAuthentication]
    # permission_classes      = [IsOwner]
    serializer_class        = CustomerSerializer
    queryset                = Customer.objects.all()
