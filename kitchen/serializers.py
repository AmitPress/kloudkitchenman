from rest_framework import serializers
from kitchen.models import Kitchen, Item, Category, Modifier, Menu
class KitchenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitchen
        fields = "__all__"

class ModifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modifier
        fields = "__all__"

class ItemSerializer(serializers.ModelSerializer):
    modifiers = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = "__all__"
    def get_modifiers(self, obj):
        return obj.modifiers.values_list("id", flat=True)

class CategorySerializer(serializers.ModelSerializer):
    # items = ItemSerializer(many=True, read_only=True)
    items = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = "__all__"
    def get_items(self, obj):
        return obj.items.values_list("id", flat=True)
class MenuSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    class Meta:
        model = Menu
        fields = "__all__"
    def get_items(self, obj):
        return obj.items.values_list("id", flat=True)