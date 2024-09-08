from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from stakeholders.permissions import IsOwner, IsEmployee, IsCustomer, IsSuperuser, HasCustomerGET, HasCustomerPUT, HasCustomerPATCH, HasCustomerDELETE, HasGuestPOST
from stakeholders.serializers import OwnerSerializer, EmployeeSerializer, CustomerSerializer, UserSigninSerializer
from stakeholders.models import User, Owner, Employee, Customer

# crud viewset

class OwnerViewSet(ModelViewSet):
    authentication_classes  = [TokenAuthentication]
    permission_classes      = [IsSuperuser] # only a super user can literally do anything to an owner
    serializer_class        = OwnerSerializer
    queryset                = Owner.objects.all()


class EmployeeViewSet(ModelViewSet):
    authentication_classes  = [TokenAuthentication]
    permission_classes      = [IsOwner] # only owners can create emplotee
    serializer_class        = EmployeeSerializer
    queryset                = Employee.objects.all()


class CustomerViewSet(ModelViewSet):
    authentication_classes  = [TokenAuthentication]
    permission_classes      = [HasCustomerGET, HasCustomerPUT, HasCustomerPATCH, HasCustomerDELETE]
    serializer_class        = CustomerSerializer
    queryset                = Customer.objects.all()


# user signin

class UserSigninViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = UserSigninSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "userid": user.id,
            "username": user.username,
            "token": token.key
        })
    
# only customer signup

class CustomerSignupViewSet(GenericViewSet, CreateModelMixin):
    authentication_classes  = [TokenAuthentication]
    permission_classes      = [HasGuestPOST]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
