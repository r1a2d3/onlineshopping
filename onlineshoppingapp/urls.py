from django.conf.urls import url
from onlineshoppingapp import views
urlpatterns = [
	url(r'^onlineshoppingapp/$', views.HomePageView.as_view()),
	url(r'index.html', views.HomePageView.as_view()),
	url(r'iphonex1.html', views.HomePageView1.as_view()),
	url(r'cart.html', views.HomePageView2.as_view()),
	url(r'^index1', views.index),
	url(r'^select', views.select),
]