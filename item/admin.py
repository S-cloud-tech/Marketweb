from django.contrib import admin

from .models import Category, Item, StockUpdate, Supplier

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Item)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'category', 'quantity', 'low_stock_threshold', 'updated_at')
    search_fields = ('name', 'sku')
    list_filter = ('category',)

@admin.register(StockUpdate)
class StockUpdateAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity_change', 'timestamp')
    search_fields = ('product__name',)
    list_filter = ('timestamp',)