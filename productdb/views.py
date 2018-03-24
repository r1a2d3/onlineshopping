from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
from .models import Product

class ProductListView(generic.ListView):
	template_name='product_list.html'
	model = Product

def getproduct(request):
	p=Product.objects.all()
	return HttpResponseRedirect('/cartdb/cart' ,{ 'product':p})