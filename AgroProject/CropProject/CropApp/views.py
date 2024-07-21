from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import React, CropModel1, CropModel2
from . serializer import ReactSerializer, CropModel1Serializer, CropModel2Serializer

@api_view(['GET', 'POST'])
def react_view(request):
    if request.method == 'GET':
        details = [{"name": detail.name, "detail": detail.detail} for detail in React.objects.all()]
        return Response(details)
    elif request.method == 'POST':
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def CropModel1View(request):
    if request.method == 'GET':
        queryset = CropModel1.objects.all()
        serializer = CropModel1Serializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CropModel1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def CropModel2View(request):
    if request.method == 'GET':
        queryset = CropModel2.objects.all()
        serializer = CropModel2Serializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CropModel2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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