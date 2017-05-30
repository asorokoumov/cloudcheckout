from django.shortcuts import render
from checkout.models import Product, Seller, Delivery


# Create your views here.
def checkout(request, product_link):
    product = Product.objects.get(link=product_link)
    return render(request, 'checkout/product_page.html', {'product': product})

