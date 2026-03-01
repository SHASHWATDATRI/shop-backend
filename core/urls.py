"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from shop.views import product_api, artist_list, artist_detail # Teeno imports sahi hain

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Sabhi products ke liye
    path('api/products/', product_api, name='product_api'),
    
    # Sabhi artists ki list ke liye
    path('api/artists/', artist_list, name='artist_list'),
    
    # Kisi ek artist ka portfolio/creation dekhne ke liye (Jaise Aditya Singh)
    # <int:pk> ka matlab hai ki yahan artist ki ID aayegi (1, 2, 3...)
    path('api/artists/<creation>/', artist_detail, name='artist_detail'),
]
