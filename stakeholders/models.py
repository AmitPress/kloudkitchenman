from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from helpers.timestampedmodel import TimeStampedModelMixin


class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if not (username and email and password):
            raise ValueError("Either of The Inputs Are Not Given or Given Incorrectly")
        user = self.model()
        user.username = username
        user.email = self.normalize_email(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email, password):
        user = self.create_user(username=username, email=email, password=password)
        user.is_staff = True 
        user.is_superuser = True
        user.save(using=self._db)
        return user
    def create_staff(self, username, email, password):
        user = self.create_user(username=username, email=email, password=password)
        user.is_staff = True 
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModelMixin):
    class Role(models.TextChoices):
        Default     = "DEFAULT", "default"
        Owner       = "OWNER", "owner"
        Employee    = "EMPLOYEE", "employee"
        Customer    = "CUSTOMER", "customer"

    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)
    user_role           = models.CharField(max_length=20, choices=Role.choices)

    name                = models.CharField(max_length=100)
    email               = models.CharField(max_length=255, unique=True)
    password            = models.CharField(max_length=255)
    address             = models.TextField(max_length=1000)
    
    objects             = UserManager()

    USERNAME_FIELD      = "email"
    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_role = self.Role.Default
        return super().save(*args, **kwargs)
