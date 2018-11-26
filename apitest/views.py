from django.contrib import auth
from django.shortcuts import render
from apitest import views
from django.http import HttpResponse, HttpResponseRedirect
from product.models import Product


def home(request):
	return render(request, 'home.html')

def logout(request):
	auth.logout(request)
	return render(request,'login.html')

def product_manage(request):
	username = request.session.get('user','')
	prodcut_list = Product.objects.all()
	return render(request,'product_manage.html',{'user':username,'products':prodcut_list})

def login(request):
	if request.POST:
		username = passoword = ''
		username = request.POST.get('username')
		passoword = request.POST.get('password')
		user = auth.authenticate(username = username,passoword = passoword)
		if user is not None and user.is_active:
			auth.login(request,user)
			request.session['user'] = username
			response = HttpResponseRedirect('/home/')
			return response
		else:
			return render(request,'login.html',{'error':'用户名或者密码错误'})
	return render(request,'login.html')




