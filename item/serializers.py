from rest_framework import serializers
from .models import Item, StockUpdate, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Item
        fields = ['id', 'name', 'sku', 'description', 'category', 'category_id',
                  'quantity', 'low_stock_threshold', 'created_at', 'updated_at']

class StockUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockUpdate
        fields = '__all__'
