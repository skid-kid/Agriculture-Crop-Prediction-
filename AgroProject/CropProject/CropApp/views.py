from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import joblib
import numpy as np
import pandas as pd
from . models import CropModel1
from . serializer import CropModel1Serializer

@api_view(['GET', 'POST'])
def CropModel1View(request):
    if request.method == 'GET':
        queryset = CropModel1.objects.all()
        serializer = CropModel1Serializer(queryset, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        required_fields = ['Crop_Type', 'Crop_Name', 'N', 'P', 'K', 'pH', 'RainFall', 'Temperature', 'Area_in_hectares']
        missing_fields = [field for field in required_fields if field not in request.data]
        
        if missing_fields:
            return Response({field: ['This field is required.'] for field in missing_fields}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            data = {
                'Crop_Type': request.data['Crop_Type'],
                'Crop': request.data['Crop_Name'],
                'N': float(request.data['N']),
                'P': float(request.data['P']),
                'K': float(request.data['K']),
                'pH': float(request.data['pH']),
                'rainFall': float(request.data['RainFall']),
                'temperature': float(request.data['Temperature']),
                'Area_in_hectares': float(request.data['Area_in_hectares']),
                'State_Name': request.data['State_Name']
            }
        except ValueError:
            return Response({'error': 'All numeric fields must be valid numbers.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Ensure data is in the correct format for the model
        try:
            # Creating a DataFrame with the correct feature names
            features_df = pd.DataFrame([[
                data[State_Name],data['Crop_Type'], data['Crop'], data['N'], data['P'], data['K'], 
                data['pH'], data['rainFall'], data['temperature'], data['Area_in_hectares']
            ]], columns=['State_Name','Crop_Type', 'Crop', 'N', 'P', 'K', 'pH', 'rainFall', 'temperature', 'Area_in_hectares'])
            
            pipeline = joblib.load("model1.sav")
            prediction = pipeline.predict(features_df)
        except Exception as e:
            return Response({'error': f'An error occurred while loading the model or making a prediction: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({'prediction': prediction[0]}, status=status.HTTP_201_CREATED)


    
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