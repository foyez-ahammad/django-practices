from django.contrib import admin
from .models import Product, Offer, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address',
                    'product_name', 'product_items')


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Order, OrderAdmin)
