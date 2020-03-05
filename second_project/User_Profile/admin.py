from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Registration)
admin.site.register(Product)


class CartItemline(admin.TabularInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    list_display = ['user']

    fields = ['user', 'total', 'state']
    inlines = [
        CartItemline,
    ]
admin.site.register(Cart, CartAdmin)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['item', 'cart_id', 'quantity']
