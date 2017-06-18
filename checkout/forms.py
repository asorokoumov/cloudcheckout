from django import forms
from django.forms import Textarea

from .models import Customer, Order


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'phone', 'email', 'comments')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product_comments',)
        widgets = {
            'product_comments': Textarea(attrs={'class': 'textarea', 'placeholder': 'Комментарий'}),
        }


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('address',)


