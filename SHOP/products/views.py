from django.shortcuts import render
from .models import Product, Order
from django.contrib import messages


def products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})


def order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        product_name = request.POST.get('product_name')
        product_items = request.POST.get('product_items')
        details = request.POST.get('details')

        order = Order(name=name, phone=phone, address=address,
                      product_name=product_name, product_items=product_items, details=details)
        order.save()
        messages.success(request, 'Successfully, ')
    return render(request, 'products/order.html')
