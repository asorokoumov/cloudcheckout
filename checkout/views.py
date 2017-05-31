from django.shortcuts import render
from checkout.models import Product, Seller, Delivery
from .forms import CustomerDataForm
from django.shortcuts import redirect


# Create your views here.

def checkout(request, product_link):
    product = Product.objects.get(link=product_link)
    return render(request, 'checkout/product_page.html', {'product': product})


def step1(request, product_link):
    if request.method == "POST":
        form = CustomerDataForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            product = Product.objects.get(link=product_link)
            return render(request, 'checkout/product_page.html', {'product': product})

    else:
        form = CustomerDataForm()
    return render(request, 'checkout/step1.html', {'form': form})
