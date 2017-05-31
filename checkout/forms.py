from django import forms

from .models import Customer


class CustomerDataForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('name', 'phone', 'email', 'comments')