from django.conf.urls import url
from .  import views
from .views import *
from django.views.generic import TemplateView


urlpatterns=[
	url(r'^Userlogin/',GenerateRandomUserView.as_view(),name='celery_p'),
]