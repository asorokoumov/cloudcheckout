from django import forms

from .models import Customer, Order


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'phone', 'email', 'comments')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product_comments',)


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('address',)


