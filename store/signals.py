from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Product


@receiver(pre_save, sender=Product)
def update_sale_price(sender, instance: Product, **kwargs):
    if instance.sale_price == 0:
        instance.sale_price = instance.price
