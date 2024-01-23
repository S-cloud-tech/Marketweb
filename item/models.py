from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=225)

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
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    qty_supplied = models.IntegerField(default=0)
    qty_sold = models.IntegerField(default=0)
    is_sold = models.BooleanField(default=False)
    is_bad = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # price_supplied_at = models.FloatField()
    # updated_price = models.FloatField()

    def __str__(self):
        return self.name 

class Supplier(models.Model):
    name = models.CharField(max_length=225)
    commpany_name: models.CharField(max_length=255)
    contact = models.IntegerField()
    item = models.ForeignKey(Item, related_name='supplier', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
