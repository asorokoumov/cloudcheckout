from django import forms
from django.forms import Textarea
from django.forms.widgets import Input

from .models import Customer, Order


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'phone', 'email', 'comments')
        widgets = {
            'comments': Textarea(attrs={'class': 'textarea', 'placeholder': 'Комментарий'}),
            'phone': Input(attrs={'class': 'input','placeholder': 'Телефон', 'type': 'tel'}),
            'email': Input(attrs={'class': 'input', 'placeholder': 'Email', 'type': 'email'}),
            'name': Input(attrs={'class': 'input', 'placeholder': 'Имя', 'type': 'text'}),
        }


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


