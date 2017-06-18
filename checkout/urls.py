from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^product/(?P<product_link>[-\w]+)/$', views.checkout_product, name='checkout_product'),
    url(r'^(?P<order_nr>[-\w]+)/contacts', views.checkout_contacts, name='checkout_contacts'),
    url(r'^(?P<order_nr>[-\w]+)/production', views.checkout_production, name='checkout_production'),
    url(r'^(?P<order_nr>[-\w]+)/delivery', views.checkout_delivery, name='checkout_delivery'),
    url(r'^(?P<order_nr>[-\w]+)/success', views.checkout_success, name='checkout_success'),
]