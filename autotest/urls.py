
from django.contrib import admin
from django.urls import path
from apitest import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login),
    path('home/',views.home),
	path('logout/',views.logout),
	path('product_manage/',views.product_manage)
]
