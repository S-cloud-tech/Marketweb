from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import StockUpdate, Product

@receiver(post_save, sender=StockUpdate)
def update_product_quantity(sender, instance, created, **kwargs):
    """
    After saving a StockUpdate, adjust the product's quantity.
    """
    if created:
        product = instance.product
        product.quantity += instance.quantity_change
        product.save()
