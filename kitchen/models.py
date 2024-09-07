from django.db import models
from helpers.timestampedmodel import TimeStampedModelMixin
# Create your models here.

class Kitchen(models.Model, TimeStampedModelMixin):
    name            = models.CharField(max_length=128)
    registration    = models.CharField(max_length=256)
    location        = models.TextField(max_length=1024)
    latitude        = models.FloatField(max_length=100)
    longitude       = models.FloatField(max_length=200)
    inagurated      = models.DateField(auto_now_add=False)
    opens_at        = models.DateField(auto_now_add=False)
    closes_at       = models.DateField(auto_now_add=False)
    owner           = models.ForeignKey("stakeholders.Owner", on_delete=models.SET_NULL, null=True, related_name="kitchens")

class Item(models.Model, TimeStampedModelMixin):
    class Status(models.TextChoices):
        Available   = "AVAILABLE", "available"
        OutOfStock  = "OUTOFSTOCK", "outofstock"
    
    name            = models.CharField(max_length=128)
    description     = models.TextField(max_length=1024)
    price           = models.FloatField(default=0.0)
    discount        = models.FloatField(default=0.0)
    categories      = models.ManyToManyField("Category", on_delete=models.SET_NULL, null=True, related_name="items")
    status          = models.CharField(max_length=255, choices=Status.choices, default=Status.Available)

class Category(models.Model, TimeStampedModelMixin0):
    class Status(models.TextChoices):
        Available   = "AVAILABLE", "available"
        OutOfStock  = "OUTOFSTOCK", "outofstock"
    class MealType(models.TextChoices):
        Breakfast   = "BREAKFAST", "breakfast"
        Brunch      = "BRUNCH", "brunch"
        Lunch       = "LUNCH", "lunch"
        Lupper      = "LUPPER", "lupper"
        Supper      = "SUPPER", "supper"
        Dinner      = "DINNER", "dinner"

    meal_type       = models.CharField(max_length=128, choices=MealType.choices, default=None, null=True)
    name            = models.CharField(max_length=256)
    discount        = models.FloatField(default=0.0)
    status          = models.CharField(max_length=256, choices=Status.choices, default=Status.Available) 

class Modifiers(models.Model, TimeStampedModelMixin0):
    class Status(models.TextChoices):
        Available   = "AVAILABLE", "available"
        OutOfStock  = "OUTOFSTOCK", "outofstock"
    name            = models.CharField(max_length=256)
    price           = models.FloatField(default=0.0)
    discount        = models.FloatField(default=0.0)
    status          = models.CharField(max_length=256, choices=Status.choices, default=Status.Available)
    items           = models.ManyToManyField("Item", on_delete=models.SET_NULL, null=True, related_name="modifiers")



