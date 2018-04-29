from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
from .models import Order
from cartdb.models import Cart
from productdb.models import Product
import datetime
from django.contrib.auth.decorators import login_required

@login_required(login_url='/loginmodule/login/')
def placeorder(request):
	c={}
	c.update(csrf(request))
	return render(request,'billinginfo.html', )

@login_required(login_url='/loginmodule/login/')	
def addorderdetail(request):
	name =request.POST.get('name','')
	mobileno = request.POST.get('mo.no.','')
	area = request.POST.get('area','')
	landmark = request.POST.get('landmark','')
	buldingname = request.POST.get('bname','')
	city = request.POST.get('city','')
	state = request.POST.get('state','')
	pincode = request.POST.get('pincode','')
	add =[]
	add.append(name)
	add.append(mobileno)
	add.append(area)
	add.append(buldingname)
	add.append(landmark)
	add.append(city)
	add.append(state)
	add.append(pincode)
	request.session['address']=add;
	userid=request.session.get('userid')
	cart = Cart.objects.filter(username=userid)
	pid=[]
	for p in cart:
		pid.append(p.productid)
	product = Product.objects.filter(productid__in=pid)
	tp=0
	for pr in product:
		tp+=pr.price
	dd=datetime.date.today() + datetime.timedelta(days=7)
	return render(request,'orderinfo.html' ,{'address':add , 'cart1':cart,'product1':product,'tprice':tp,'ddate':dd})

@login_required(login_url='/loginmodule/login/')
def ordersuccess(request):
	add=request.session.get('address')
	dd=datetime.date.today() + datetime.timedelta(days=7)
	ordertime=datetime.datetime.now()
	userid=request.session.get('userid')
	name=add[0]
	mobileno=add[1]
	area=add[2]
	buldingname=add[3]
	landmark=add[4]
	city=add[5]
	state=add[6]
	pincode=add[7]
	cart = Cart.objects.filter(username=userid)
	pid=[]
	for p in cart:
		pid.append(p.productid)
	for p in cart:
		o=Order(userid=userid,name=name,mobileno=mobileno,area=area,buldingname=buldingname,landmark=landmark,city=city,state=state,pincode=pincode,productid=p.productid,ddate=dd)
		o.save()
	o1=Cart.objects.filter(productid__in=pid).delete()
	return render(request,'ordersuccess.html',{'ddate':dd,'address':add})

@login_required(login_url='/loginmodule/login/')
def vieworder(request):
	userid=request.session.get('userid')
	o=Order.objects.filter(userid=userid)
	pid=[]
	for p in o:
		pid.append(p.productid)
	p=Product.objects.filter(productid__in=pid)
	td=datetime.date.today()
	return render(request,'myorder.html',{'pro':p,'ord':o,'today':td})


@login_required(login_url='/loginmodule/login/')
def orderdetail(request):
	userid=request.session.get('userid')
	return render_to_response('order_list.html',{'order1' : o , 'userid' : request.session.get('userid')} )

class OrderListView(generic.ListView):
	template_name='order_list.html'
	model = Order