from django.db import models 

class React(models.Model): 
    name = models.CharField(max_length=30) 
    detail = models.CharField(max_length=500)

class CropModel1(models.Model):
    State_name=models.CharField(max_length=30,null=True)
    Crop_Type=models.CharField(max_length=30)
    Crop=models.CharField(max_length=30)
    N=models.IntegerField()
    P=models.IntegerField()
    K=models.IntegerField()
    pH=models.FloatField(max_length=5)
    rainfall=models.FloatField(max_length=5)
    temperature=models.FloatField(max_length=5)
    Area_in_hectares=models.FloatField(max_length=10)

class CropModel2(models.Model):
    Nitrogen=models.IntegerField(null=True)
    Phosphorus=models.IntegerField(null=True)
    Potassium=models.IntegerField(null=True)
    Temperature=models.FloatField(max_length=5,null=True)
    Humidity=models.FloatField(max_length=5,null=True)
    pH_Value=models.FloatField(max_length=5,null=True)
    Rainfall=models.FloatField(max_length=5,null=True)
    
