from django.contrib import admin 
from django.urls import path, include 
from django.urls import re_path
from CropApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crops1/', CropModel1View),
    path('crops2/', CropModel2View),
]
