from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^signup/$', views.signup),
	url(r'^adduser/$', views.adduser),
]