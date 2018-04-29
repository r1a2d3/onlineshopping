from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
from productdb.models import Product
from django.contrib.auth.decorators import login_required

@login_required(login_url='/loginmodule/login/')
def index(request):
	cat=request.POST.get('cat','')
	if cat!='':
		p1=Product.objects.filter(category=cat)
	else:
		p1=Product.objects.all()
	return render(request, 'index1.html', {'product1' : p1})

@login_required(login_url='/loginmodule/login/')
def select(request):
	pid=request.POST.get('productid','')
	p1=Product.objects.filter(productid=pid)
	return render(request, 'select.html', {'product1': p1})
	
class HomePageView(TemplateView):
	template_name='index.html'
	def post(self, request):
		return render(request, 'index.html', context=None)
class HomePageView1(TemplateView):
	template_name='iphonex1.html'
	def post(self, request):
		return render(request, 'iphonex1.html', context=None)
class HomePageView2(TemplateView):
	template_name='cart.html'
	def post(self, request):
		HttpResponseRedirect('/orderdb/placeorder/')

# Create your views here.
