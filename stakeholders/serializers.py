from rest_framework import serializers
from rest_framework.authentication import authenticate
from stakeholders.models import Owner, Employee, Customer

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        exclude = ["is_staff", "is_superuser", "last_login", "user_role"]

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ["is_staff", "is_superuser", "last_login", "user_role"]

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ["is_staff", "is_superuser", "last_login", "user_role"]

class UserSigninSerializer(serializers.Serializer):
    email    = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if not email:
            raise serializers.ValidationError("Email Not Provided")
        if not password:
            raise serializers.ValidationError("Password Not Provided")
        user = authenticate(email=email, password=password)
        if user:
            data['user'] = user
        else:
            raise serializers.ValidationError("Signup Failed Due To Unmatched Credential")
        return data