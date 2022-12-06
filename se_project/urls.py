"""se_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from car_rent.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rent/', rent),
    path('report/', report),
    path('transaction/',transaction),
    path('transaction_detail/',transaction_detail),
    path('order/',order),
    path('return_car/',return_car),
    path('personal_info/',personal_info),
    path('personal_info_update/',personal_info_update)
]
