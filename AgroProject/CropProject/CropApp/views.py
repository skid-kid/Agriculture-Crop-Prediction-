from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import joblib
import numpy as np
import pandas as pd
from . models import CropModel1,CropModel2
from . serializer import CropModel1Serializer,CropModel2Serializer

@api_view(['GET', 'POST'])
def CropModel1View(request):
    if request.method == 'GET':
        queryset = CropModel1.objects.all()
        serializer = CropModel1Serializer(queryset, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        required_fields = ['State_Name','Crop_Type', 'Crop', 'N', 'P', 'K', 'pH', 'rainfall', 'temperature', 'Area_in_hectares']
        missing_fields = [field for field in required_fields if field not in request.data]
        
        if missing_fields:
            return Response({field: ['This field is required.'] for field in missing_fields}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            data = {
                'State_Name': request.data['State_Name'],
                'Crop_Type': request.data['Crop_Type'],
                'Crop': request.data['Crop'],
                'N': float(request.data['N']),
                'P': float(request.data['P']),
                'K': float(request.data['K']),
                'pH': float(request.data['pH']),
                'rainfall': float(request.data['rainfall']),
                'temperature': float(request.data['temperature']),
                'Area_in_hectares': float(request.data['Area_in_hectares']),
            }
        except ValueError:
            return Response({'error': 'All numeric fields must be valid numbers.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Ensure data is in the correct format for the model
        try:
            # Creating a DataFrame with the correct feature names
            features_df = pd.DataFrame([[
                data['State_Name'],data['Crop_Type'], data['Crop'], data['N'], data['P'], data['K'], 
                data['pH'], data['rainfall'], data['temperature'], data['Area_in_hectares']
            ]], columns=['State_Name','Crop_Type', 'Crop', 'N', 'P', 'K', 'pH', 'rainfall', 'temperature', 'Area_in_hectares'])
            
            pipeline = joblib.load("model1.sav")
            prediction = pipeline.predict(features_df)
        except Exception as e:
            return Response({'error': f'An error occurred while loading the model or making a prediction: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({'prediction': prediction[0]}, status=status.HTTP_201_CREATED)

from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder

# Load the model and LabelEncoder at startup
model = load_model('model.h5')

# Load the LabelEncoder
le = LabelEncoder()
df = pd.read_csv('C:\\Users\\hp\\Agriculture-Crop-Prediction-\\ML Models\\Crop_Recommendation.csv')
le.fit(df['Crop'])

@api_view(['GET', 'POST'])
def CropModel2View(request):
    if request.method == 'GET':
        queryset = CropModel2.objects.all()
        serializer = CropModel2Serializer(queryset, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CropModel2Serializer(data=request.data)
        if serializer.is_valid():
            # Save the validated data
            serializer.save()

            # Extract features for prediction
            input_data = np.array([[
                serializer.validated_data['Nitrogen'],
                serializer.validated_data['Phosphorus'],
                serializer.validated_data['Potassium'],
                serializer.validated_data['Temperature'],
                serializer.validated_data['Humidity'],
                serializer.validated_data['pH_Value'],
                serializer.validated_data['Rainfall']
            ]])

            # Make prediction
            prediction = model.predict(input_data)
            predicted_class = np.argmax(prediction, axis=1)
            crop = le.inverse_transform(predicted_class)[0]

            # Add prediction to the response
            response_data = serializer.data
            response_data['predicted_crop'] = crop
            
            return Response(response_data, status=status.HTTP_201_CREATED)
        
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