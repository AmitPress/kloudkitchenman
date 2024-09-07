from rest_framework import serializers
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