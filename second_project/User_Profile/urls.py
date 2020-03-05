from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^registration$', views.Registration_View, name='registration'),
    url(r'^login$', views.Login_View, name='login'),
    url(r'^logout$', views.log_out, name='logout'),
    url(r'^view$', views.view_profile, name='view'),
    url(r'^update$', views.Update_View, name='update'),
    url(r'^delete$', views.delete_account, name='delete'),
    url(r'^product$', views.product_detail, name='product'),
    url(r'^cart/(?P<product_id>\d+)/$', views.view_carts, name='view_cart'),
    url(r'^showcart$', views.cart_details, name='showcart'),
    url(r'^remove/$', views.remove_item, name='remove'),
    url(r'^quantity/$', views.update_quantity, name='quantity'),
    url(r'^checkout/$', views.Checkout, name='checkout'),
    url(r'^pay/(?P<cart_id>\d+)/$', views.payment, name='pay'),
]
