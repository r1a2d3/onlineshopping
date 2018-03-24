from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^addtocart', views.addtocart),
	url(r'^viewcart/$', views.viewcart),
	url(r'^cart/',views.cart),
	#url('cart/', views.CartListView.as_view(), name ='cart'),
	url('delete', views.delete),
]