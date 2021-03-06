"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('add_cart/', views.add_cart),
    path('cart/', views.cart),
    path('cart_option/', views.cart_option),
    path('order/', views.order),
    path('add_order/', views.add_order),
    path('reset/', views.reset_pwd),
]
