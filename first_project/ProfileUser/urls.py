from django.conf.urls import url
from .  import views
from . views import *
from django.views.generic import TemplateView


urlpatterns=[
	url(r'^login$',views.Profile_User,name='profile'),
	url(r'^signin$',views.User_login,name='log'),
]
