from django.conf.urls import url
from .  import views
from . views import *
from django.views.generic import TemplateView


urlpatterns=[
	url(r'^registration$',views.Registration_View,name='registration'),
	
]