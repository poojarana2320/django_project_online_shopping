from django.conf.urls import url
from .  import views
from . views import *
from django.views.generic import TemplateView


urlpatterns=[
 	url(r'^home$',TemplateView.as_view(template_name='myapp/review_booking.html')),
	url(r'^r$',views.responseform,name='response'),
	url(r'^d$',views.AirDetails,name='detail'),
	# url(r'a$',views.AirDetails,name='air')
]