from rest_framework import serializers 
from . models import *
  
class ReactSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = React 
        fields = ['name', 'detail'] 

class CropModel1Serializer(serializers.ModelSerializer):
    class Meta:
        model = CropModel1
        fields = '__all__'

class CropModel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = CropModel2
        fields = '__all__'