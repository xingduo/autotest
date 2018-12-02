from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apitest import views
from django.http import HttpResponse, HttpResponseRedirect
from product.models import Product
from apitest.models import Apistep,Apitest

def home(request):
	return render(request, 'home.html')

def logout(request):
	auth.logout(request)
	return render(request,'login.html')

def product_manage(request):
	username = request.session.get('user','')
	prodcut_list = Product.objects.all()
	return render(request,'product_manage.html',{'user':username,'products':prodcut_list})

#接口管理
@login_required
def apitest_manage(request):
	apitest_list = Apitest.objects.all()#读取所有接口数据
	username = request.session.get('user','')#读取浏览器登录session
	return render(request,'apitest_manage.html',{'user':username,'apitests':apitest_list})
    #定义流程接口数据的变量并返回到前端

#接口步骤管理
@login_required
def apistep_manage(request):
	username = request.session.get('user','')
	apistep_list = Apistep.objects.all()
	return render(request,'apistep_manage.html',{'user':username,'apisteps':apistep_list})


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




