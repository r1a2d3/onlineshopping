from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
from .models import Cart
from productdb.models import Product
from django.contrib.auth.decorators import login_required

@login_required(login_url='/loginmodule/login/')
def addtocart(request):
	username = request.session.get('userid')
	productid1 = request.POST.get('productid', '')
	s=Cart(username=username,productid=productid1)
	s.save()
	f=request.POST.get('buy now','')
	if(f=='BUY NOW'):
		return HttpResponseRedirect('/orderdb/placeorder')
	else:
		return HttpResponseRedirect('/onlineshoppingapp/index1')

@login_required(login_url='/loginmodule/login/')
def viewcart(request):
	product = Product.objects.all()
	return HttpResponseRedirect('/productdb/getproduct')

@login_required(login_url='/loginmodule/login/')
def cart(request):
	userid=request.session.get('userid')
	cart = Cart.objects.filter(username=userid)
	pid=[]
	for p in cart:
		pid.append(p.productid)
	product = Product.objects.filter(productid__in=pid)
	tp=0
	for pr in product:
		tp+=pr.price
	return render(request,'cart_list.html',{'cart1' : cart , 'product1' : product ,'tprice':tp})

@login_required(login_url='/loginmodule/login/')
def delete(request):
	productid= request.GET.get('productid','')
	s1 = Cart.objects.filter(productid=productid).delete()
	return HttpResponseRedirect('/cartdb/cart/')
	
class CartListView(generic.ListView):
	template_name='cart_list.html'
	model = Cart
	
