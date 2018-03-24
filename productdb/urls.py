from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	url('products/', views.ProductListView.as_view(), name ='products'),
	url(r'^getproduct/$',views.getproduct)
]