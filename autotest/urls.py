
from django.contrib import admin
from django.urls import path
from apitest import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login),
    # path(r'^home/$',views.home)
]
