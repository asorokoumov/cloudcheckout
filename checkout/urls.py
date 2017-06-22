from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^product/(?P<seller_name>[-@./#&+\w\s]+)/(?P<product_link>[-@./#&+\w\s]+)/$', views.checkout_product, name='checkout_product'),
    url(r'^(?P<order_nr>[-\w]+)/contacts', views.checkout_contacts, name='checkout_contacts'),
    url(r'^(?P<order_nr>[-\w]+)/production', views.checkout_production, name='checkout_production'),
    url(r'^(?P<order_nr>[-\w]+)/delivery', views.checkout_delivery, name='checkout_delivery'),
    url(r'^(?P<order_nr>[-\w]+)/success', views.checkout_success, name='checkout_success'),
    url(r'^seller/login', views.seller_login, name='seller_login'),
    url(r'^seller/logout', views.seller_logout, name='seller_logout'),
    url(r'^seller/register', views.seller_register, name='seller_register'),
    url(r'^seller/', views.seller_space, name='seller_space'),

    #TODO add default path
]