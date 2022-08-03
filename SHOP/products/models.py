from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=3000)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=300)
    discount = models.FloatField()


class Order(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    product_name = models.CharField(max_length=2000)
    product_items = models.CharField(max_length=10)
    details = models.TextField()
