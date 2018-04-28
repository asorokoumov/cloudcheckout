from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static, settings

urlpatterns = [
    url(r'^product/(?P<product_link>[-@./#&+\w\s]+)/$', views.checkout_product, name='checkout_product'),
    url(r'^(?P<order_nr>[-\w]+)/contacts/$', views.checkout_contacts, name='checkout_contacts'),
    url(r'^(?P<order_nr>[-\w]+)/production/$', views.checkout_production, name='checkout_production'),
    url(r'^(?P<order_nr>[-\w]+)/delivery/$', views.checkout_delivery, name='checkout_delivery'),
    url(r'^(?P<order_nr>[-\w]+)/success/$', views.checkout_success, name='checkout_success'),
    url(r'^/$', views.in_development, name='in_development'),
    url(r'^$', views.in_development, name='in_development'),
    #    url(r'^seller/login/$', views.seller_login, name='seller_login'),
#    url(r'^seller/logout/$', views.seller_logout, name='seller_logout'),
#    url(r'^seller/register/$', views.seller_register, name='seller_register'),
#    url(r'^seller/products/add/$', views.seller_products_add, name='seller_products_add'),
#    url(r'^seller/products/$', views.seller_products, name='seller_products'),
#    url(r'^seller/products/edit/(?P<product_link>[-@./#&+\w\s]+)/$', views.seller_products_edit, name='seller_products_edit'),
#    url(r'^seller/products/delete/(?P<product_link>[-@./#&+\w\s]+)/$', views.seller_products_delete, name='seller_products_delete'),
#    url(r'^seller/$', views.seller_space, name='seller_space'),

    #TODO add default path
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
