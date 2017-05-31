from django.shortcuts import render
from checkout.models import Product, Seller, Delivery, Order
from .forms import ContactsForm, ProductForm, DeliveryForm
from django.shortcuts import redirect


# Create your views here.

def checkout_product(request, product_link):
    product = Product.objects.get(link=product_link)
    if request.method == "POST":
        checkout_form = ProductForm(request.POST)
        if checkout_form.is_valid():
            order = checkout_form.save(commit=False)
            order.order_nr = generate_order_nr()
            order.product = Product.objects.get(link=product_link)
            order.save()
            return redirect('checkout_contacts', order_nr=order.order_nr)

    else:
        checkout_form = ProductForm()
    return render(request, 'checkout/product.html', {'product': product, 'form': checkout_form})


def generate_order_nr():
    return '123-3'


def checkout_contacts(request, order_nr):
    if request.method == "POST":
        form = ContactsForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()

            order = Order.objects.filter(order_nr=order_nr).order_by('-id')[0]
            order.customer = customer
            order.save()
            return redirect('checkout_delivery', order_nr=order.order_nr)

    else:
        form = ContactsForm()
    return render(request, 'checkout/contacts.html', {'form': form})


def checkout_delivery(request, order_nr):
    if request.method == "POST":
        form = DeliveryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            order = Order.objects.filter(order_nr=order_nr).order_by('-id')[0]
            order.address = data['address']
            order.save()
            return redirect('checkout_success', order_nr=order.order_nr)
    else:
        form = DeliveryForm()
    return render(request, 'checkout/delivery.html', {'form': form})


def checkout_success(request, order_nr):
    order = Order.objects.filter(order_nr=order_nr).order_by('-id')[0]
    return render(request, 'checkout/success.html', {'order': order})
