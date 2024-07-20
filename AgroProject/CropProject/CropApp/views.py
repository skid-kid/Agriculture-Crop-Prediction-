from django.shortcuts import render 
from rest_framework.views import APIView 
from . models import *
from rest_framework.response import Response 
from . serializer import *
from rest_framework import viewsets
from rest_framework import status
# Create your views here. 
  
class ReactView(APIView): 
    
    serializer_class = ReactSerializer 
  
    def get(self, request): 
        detail = [ {"name": detail.name,"detail": detail.detail}  
        for detail in React.objects.all()] 
        return Response(detail) 
  
    def post(self, request): 
  
        serializer = ReactSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return  Response(serializer.data) 

class CropModel1ViewSet(viewsets.ModelViewSet):
    queryset = CropModel1.objects.all()
    serializer_class = CropModel1Serializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            print('Validation errors:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CropModel2ViewSet(viewsets.ModelViewSet):
    queryset = CropModel2.objects.all()
    serializer_class = CropModel2Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""class CropModel2ViewSet(viewsets.ModelViewSet):
    queryset = CropModel2.objects.all()
    serializer_class = CropModel2Serializer
    def get(self, request): 
        crop = [ {
            "N": crop.N,
            "P": crop.P,
            "K": crop.K,
            "pH": crop.pH,
            "EC": crop.EC,
            "OC": crop.OC,
            "S": crop.S,
            "Zn": crop.Zn,
            "Fe": crop.Fe,
            "Cu": crop.Cu,
            "Mn": crop.Mn,
            "B": crop.B}  
        for crop in React.objects.all()] 
        return Response(crop) 
    
    def post(self, request): 
  
        serializer = ReactSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return  Response(serializer.data)"""