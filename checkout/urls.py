from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^checkout/(?P<product_link>[-\w]+)/', views.checkout, name='checkout'),
]