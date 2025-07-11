from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=225, unique=True)
    description = models.TextField(blank=True, null=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=50, unique=True, default=0) #Stock keeping unit
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    quantity = models.IntegerField(default=0)
    qty_supplied = models.IntegerField(default=0)
    qty_sold = models.IntegerField(default=0)
    is_sold = models.BooleanField(default=False)
    is_bad = models.BooleanField(default=False)
    low_stock_threshold = models.IntegerField(default=5)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price_supplied_at = models.FloatField(default=0)
    updated_price = models.FloatField(default=0)


    def is_low_stock(self):
        return self.quantity <= self.low_stock_threshold

    def __str__(self):
        return self.name 


class StockUpdate(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='stock_updates')
    quantity_change = models.IntegerField(help_text="Positive for restock, negative for sales/adjustment")
    timestamp = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name}: {self.quantity_change} @ {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


class Supplier(models.Model):
    name = models.CharField(max_length=225)
    commpany_name = models.CharField(max_length=255, default=False)
    contact = models.IntegerField()
    item = models.ForeignKey(Item, related_name='supplier', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
