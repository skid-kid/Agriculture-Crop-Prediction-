"""
URL configuration for CropProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
"""
from django.contrib import admin 
from django.urls import path, include 
from django.urls import re_path
from rest_framework.routers import DefaultRouter
from CropApp.views import *

router = DefaultRouter()
router.register(r'crops', CropModel1View)
router.register(r'crops', CropModel2View)
  
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('CropModel1/', CropModel1View, name="CropModel1"),
    path('CropModel2/', CropModel2View, name="CropModel2"),
    path('', include(router.urls)),
]
"""
from django.contrib import admin 
from django.urls import path, include 
from django.urls import re_path
from CropApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crops1/', CropModel1View),
    path('crops2/', CropModel2View),
]
