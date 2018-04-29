from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^placeorder', views.placeorder),
	url(r'^addorderdetail/$', views.addorderdetail),
	url(r'^orderdetail/$', views.orderdetail),
	url(r'^ordersuccess/$',views.ordersuccess),
	url(r'^vieworder/$',views.vieworder),
	url('orders/', views.OrderListView.as_view(), name ='orders'),
]