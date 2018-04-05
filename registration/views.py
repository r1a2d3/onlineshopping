from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
from .models import Userdata
from django.contrib.auth.models import User

def signup(request):
	return render(request,'signup.html')
	
def adduser(request):
	uname=request.POST.get('name','')
	mono=request.POST.get('mo.no.','')
	email=request.POST.get('email','')
	password=request.POST.get('password','')
	u=User(username=uname)
	u.set_password(password)
	u.save()
	u1=Userdata(userid=uname,mono=mono,email=email,password=password)
	u1.save()
	return HttpResponseRedirect('/loginmodule/login')
	

