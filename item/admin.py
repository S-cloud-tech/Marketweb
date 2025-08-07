from django.contrib import admin

from .models import Category, Item, StockUpdate, Supplier

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Item)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'low_stock_threshold', 'updated_at')
    search_fields = ('name', )
    list_filter = ('updated_at', 'name',)
    ordering = ('name', 'category', 'quantity',)

@admin.register(StockUpdate)
class StockUpdateAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity_change', 'timestamp')
    search_fields = ('product__name',)
    list_filter = ('timestamp',)