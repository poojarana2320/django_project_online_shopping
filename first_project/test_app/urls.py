# from django.urls import include
# from django.conf.urls import url
# from .views import *

# urlpatterns = [
#     url(r'demo',views.Author_view,name='Author'),
#     # url(r'^class/$', Author_view_class.as_view()),
# ]

from django.conf.urls import url
from .  import views

urlpatterns=[
	url(r'demo$',views.Author_view,name='Author'),
	# url(r'p$',views.Publisher_view,name='Publisher'),
	# url(r'^class/$', views.Book_view_class.as_view()),
]