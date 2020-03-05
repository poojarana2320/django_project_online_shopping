import os
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import *
from .views import *

""" Delete old image from folder"""


@receiver(post_save, sender=Registration)
def delete_old_image(sender, instance, created, **kwargs):
    if instance.profile_image:
        path = instance._oldimage.path
        if os.path.isfile(path):
            os.remove(path)

""" Total update when admin change quantity in database """


@receiver(post_save, sender=CartItem)
def update_total(sender, instance, **kwargs):
    cart = Cart.objects.get(id=instance.cart_id.id)
    cartitem_list = CartItem.objects.filter(cart_id=cart)
    total = 0
    for cart_item in cartitem_list:
        total += (cart_item.item.price * cart_item.quantity)
    cart.total = total
    cart.save()

""" Change total after remove items """


@receiver(post_delete, sender=CartItem)
def remove_total(sender, instance, **kwargs):
    item_total = instance.item.price * instance.quantity
    cart = Cart.objects.get(id=instance.cart_id.id)
    cart.total -= item_total
    cart.save()
