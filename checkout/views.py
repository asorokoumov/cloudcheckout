from django.shortcuts import render
from checkout.models import Product, Seller, Delivery, Order
from .forms import ContactsForm, ProductForm, DeliveryForm, ProductionForm
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.models import User
import random, string


# Create your views here.

def checkout_product(request, product_link, seller_name):
    seller = Seller.objects.get(instagram=seller_name)
    product = Product.objects.get(link=product_link, seller=seller)
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
            return redirect('checkout_production', order_nr=order.order_nr)

    else:
        form = ContactsForm()
    return render(request, 'checkout/contacts.html', {'form': form})


def checkout_delivery(request, order_nr):
    if request.method == "POST":
        form = ProductionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            order = Order.objects.filter(order_nr=order_nr).order_by('-id')[0]
        #   order.address = data['address']
            order.save()
            return redirect('checkout_success', order_nr=order.order_nr)
    else:
        form = ProductionForm()
    return render(request, 'checkout/delivery.html', {'form': form})


def checkout_production(request, order_nr):
    if request.method == "POST":
        form = DeliveryForm(request.POST)
        if form.is_valid():
            order = Order.objects.filter(order_nr=order_nr).order_by('-id')[0]
            if 'now' in request.POST:
                return redirect('checkout_delivery', order_nr=order.order_nr)
            elif 'later' in request.POST:
                return redirect('checkout_success', order_nr=order.order_nr)
    else:
        form = DeliveryForm()
    return render(request, 'checkout/production.html', {'form': form})


def checkout_success(request, order_nr):
    order = Order.objects.filter(order_nr=order_nr).order_by('-id')[0]
    return render(request, 'checkout/success.html', {'order': order})


def seller_space(request):
    if auth.get_user(request).username:
        return render(request, 'checkout/seller_space.html', {'username': auth.get_user(request).username})
    else:
        return redirect('seller_login')


def seller_login(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('seller_space')
        else:
            return render(request, 'checkout/seller_login.html', {'login_error': 'Пользователь не найден'})
    else:
        return render(request, 'checkout/seller_login.html')


def seller_logout(request):
    auth.logout(request)
    return render(request, 'checkout/seller_login.html')


def seller_register(request):
    if not auth.get_user(request).username:
        return render(request, 'checkout/seller_register.html')
    else:
        if request.method == "POST":
            username = request.POST.get('username', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')

            if User.objects.filter(username=username):
                return render(request, 'checkout/seller_register.html', {'register_error': 'Пользователь уже существует'})
            elif User.objects.filter(email=email):
                return render(request, 'checkout/seller_register.html',
                              {'register_error': 'Пользователь с таким email уже существует'})
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                Seller(login=username, email=email).save()
                auth.login(request, user)
                return redirect('seller_space')
        else:
            return render(request, 'checkout/seller_space.html', {'username': auth.get_user(request).username})


def seller_products(request):
    if auth.get_user(request).username:
        seller = Seller.objects.get(login=auth.get_user(request).username)
        products = Product.objects.filter(seller=seller)
        return render(request, 'checkout/seller_products.html', {'username': auth.get_user(request).username,
                                                                 'products': products})
    else:
        return redirect('seller_login')


def seller_products_delete(request, product_link):
    if auth.get_user(request).username:
        seller = Seller.objects.get(login=auth.get_user(request).username)
        products = Product.objects.filter(seller=seller, link=product_link)
        if products:
            products.delete()
        return redirect('seller_products')

    else:
        return redirect('seller_login')


def seller_products_edit(request, product_link):

    if not auth.get_user(request).username:
        return redirect('seller_login')
    else:
        if request.method == "POST":
            title = request.POST.get('title', '')
            description = request.POST.get('description', '')
            price = request.POST.get('price', '')
            link = request.POST.get('link', '')
            development = request.POST.get('development', '')

            product = Product.objects.get(link=link)

#TODO fix case without updated image
            if request.FILES['image-file']:
                file = request.FILES['image-file']
                extension = file.name.split(".")[-1].lower()
                file.name = link + '.' + extension
                product.image = file

            product.title = title
            product.description = description
            product.price = price
            product.development = development

            product.save()
            return redirect('seller_products')
        else:
            seller = Seller.objects.get(login=auth.get_user(request).username)
            product = Product.objects.get(seller=seller, link=product_link)
            return render(request, 'checkout/seller_products_edit.html', {'username': auth.get_user(request).username,
                          'product': product})


def generate_product_link(username):
    size = 4
    chars = string.ascii_lowercase + string.digits
    seller = Seller.objects.get(login=username)
    return str(seller.id)+''.join(random.choice(chars) for _ in range(size))


def seller_products_add(request):
    if not auth.get_user(request).username:
        return redirect('seller_login')
    else:
        if request.method == "POST":
            title = request.POST.get('title', '')
            description = request.POST.get('description', '')
            price = request.POST.get('price', '')
            link = request.POST.get('link', '')
            development = request.POST.get('development', '')
            file = request.FILES['image-file']
            extension = file.name.split(".")[-1].lower()
            seller = Seller.objects.get(login=auth.get_user(request).username)
            file.name = link+'.'+extension

            product = Product(seller=seller, title=title, description=description, price=price, link=link, image=file,
                              development=development)
            product.save()
            return redirect('seller_products')
        else:
            return render(request, 'checkout/seller_products_add.html',
                      {'username': auth.get_user(request).username,
                       'link': generate_product_link(auth.get_user(request).username)})


