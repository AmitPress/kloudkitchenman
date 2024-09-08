from django.db import models
from helpers.timestampedmodel import TimeStampedModelMixin
# Create your models here.

class Kitchen(models.Model, TimeStampedModelMixin):
    name            = models.CharField(max_length=128) # TYPICAL DETAILS
    registration    = models.CharField(max_length=256) # SAME AS ABOVE
    location        = models.TextField(max_length=1024) # HANDWRITTEN LOCATION
    latitude        = models.FloatField(max_length=100) # TO SHOW MARKER
    longitude       = models.FloatField(max_length=200) # TO SHOW MARKER
    inagurated      = models.DateField(auto_now_add=False) # TRACING BACK ITS ANNIVERSARY
    opens_at        = models.DateField(auto_now_add=False) # TO DEFINE THE START OF THE WORKING HOUR
    closes_at       = models.DateField(auto_now_add=False) # TO DEFINE THE END OF THE WORKING HOUR
    owner           = models.ForeignKey("stakeholders.Owner", on_delete=models.SET_NULL, null=True, related_name="kitchens") # A KITCHEN CAN HAVE AN OWNER

    def __str__(self):
        return self.name

class Item(models.Model, TimeStampedModelMixin):
    class Status(models.TextChoices):
        Available   = "AVAILABLE", "available"
        OutOfStock  = "OUTOFSTOCK", "outofstock"
    
    name            = models.CharField(max_length=128) # TYPICAL DETAILS
    description     = models.TextField(max_length=1024) # TYPICAL DETAILS
    price           = models.FloatField(default=0.0) # IT HAD TO BE A DOUBLE FIELD BUT DJANGO DOES NOT HAVE THAT
    discount        = models.FloatField(default=0.0) # FOR SEGGREGATION
    categories      = models.ManyToManyField("Category", related_name="items") # TYPICAL DETAILS
    menus           = models.ManyToManyField("Menu", related_name="items") # TYPICAL DETAILS
    status          = models.CharField(max_length=255, choices=Status.choices, default=Status.Available) # TYPICAL DETAILS

    def __str__(self):
        return self.name

class Category(models.Model, TimeStampedModelMixin):
    class MealType(models.TextChoices):
        Breakfast   = "BREAKFAST", "breakfast"
        Brunch      = "BRUNCH", "brunch"
        Lunch       = "LUNCH", "lunch"
        Lupper      = "LUPPER", "lupper"
        Supper      = "SUPPER", "supper"
        Dinner      = "DINNER", "dinner"

    meal_type       = models.CharField(max_length=128, choices=MealType.choices, default=None, null=True) # NEED FOR SEGGREGATION
    name            = models.CharField(max_length=256) # TYPICAL DETAILS
    discount        = models.FloatField(default=0.0) # TYPICAL DETAILS

    def __str__(self):
        return self.name
class Modifier(models.Model, TimeStampedModelMixin):
    class Status(models.TextChoices):
        Available   = "AVAILABLE", "available"
        OutOfStock  = "OUTOFSTOCK", "outofstock"
    name            = models.CharField(max_length=256) # TYPICAL DETAILS
    price           = models.FloatField(default=0.0) # TYPICAL DETAILS
    discount        = models.FloatField(default=0.0) # TYPICAL DETAILS
    status          = models.CharField(max_length=256, choices=Status.choices, default=Status.Available) # TYPICAL DETAILS
    items           = models.ManyToManyField("Item", related_name="modifiers") # TYPICAL DETAILS

    def __str__(self):
        return self.name
class Menu(models.Model, TimeStampedModelMixin):
    name            = models.CharField(max_length=256)
    discount        = models.FloatField(default=0.0)

    def __str__(self):
        return self.name