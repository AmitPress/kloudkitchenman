from django.db import models
from helpers.timestampedmodel import TimeStampedModelMixin
# Create your models here.

class Card(models.Model, TimeStampedModelMixin):
    class Status(models.TextChoices):
        Active      = "ACTIVE", "active"
        Inactive    = "INACTIVE", "inactive"
    class CardType(models.TextChoices):
        Debit       = "DEBIT", "debit"
        Credit      = "CREDIT", "credit"
    card_type       = models.CharField(max_length=256, choices=CardType.choices, default=CardType.Credit)
    number          = models.IntegerField()
    cvv             = models.CharField(max_length=64) 
    expiration      = models.DateField(auto_now_add=False)
    postal_code     = models.IntegerField()
    belongs_to      = models.OneToOneField("stakeholders.Customer", verbose_name=_(""), on_delete=models.CASCADE)
    status          = models.CharField(max_length=256, choices=Status.choices, default=Status.Active)

class Coupon(models.Model, TimeStampedModelMixin):
    class Status(models.TextChoices):
        Active      = "ACTIVE", "active"
        Inactive    = "INACTIVE", "inactive"
    
    name            = models.CharField(max_length=128)
    occasion        = models.TextField(max_length=512)
    discount        = models.FloatField(default=0.0)
    users           = models.ManyToManyField("stakeholders.Customer", on_delete=models.SET_NULL, null=True, related_name="coupons")
    status          = models.CharField(max_length=256, choices=Status.choices, default=Status.Active)

class Order(models.Model, TimeStampedModelMixin):
    class State(models.TextChoices):
        Placed      = "PLACED", "placed"
        Inprocess   = "INPROCESS", "inprocess"
        Delivered   = "DELIVERED", "delivered"
        Completed   = "COMPLETED", "completed"
        Discarded   = "DISCARDED", "discarded"
    status          = models.CharField(max_length=256, choices=State.choices, default=State.Placed)
    customer        = models.ForeignKey("stakeholders.Customer", on_delete=models.SET_NULL, null=True, related_name="orders")
    applied_coupon  = models.ForeignKey("Coupon", on_delete=models.SET_NULL, null=True, related_name="orders")
    total_price     = models.FloatField(default=0.0)
    discounted_price= models.FloatField(default=0.0)

class Cart(models.Model, TimeStampedModelMixin):
    order           = models.ForeignKey("Order", on_delete=models.SET_NULL, null=True, related_name="items")
    item            = models.ForeignKey("kitchen.Item", on_delete=models.SET_NULL, null=True, related_name="orders")
    count           = models.IntegerField()
