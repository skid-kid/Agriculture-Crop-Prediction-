from django.db import models 

class React(models.Model): 
    name = models.CharField(max_length=30) 
    detail = models.CharField(max_length=500)

class CropModel1(models.Model):
    Crop_type=models.CharField(max_length=30)
    Crop_name=models.CharField(max_length=30)
    N=models.IntegerField(max_length=5)
    P=models.IntegerField(max_length=5)
    K=models.IntegerField(max_length=5)
    pH=models.FloatField(max_length=5)
    Rainfall=models.FloatField(max_length=5)
    Temperature=models.FloatField(max_length=5)
    Area_in_hectares=models.FloatField(max_length=10)
    

class CropModel2(models.Model):
    N=models.IntegerField(max_length=5)
    P=models.IntegerField(max_length=5)
    K=models.IntegerField(max_length=5)
    pH=models.FloatField(max_length=5)
    EC=models.FloatField(max_length=5)
    OC=models.FloatField(max_length=5)
    S=models.FloatField(max_length=5)
    Zn=models.FloatField(max_length=5)
    Fe=models.FloatField(max_length=5)
    Cu=models.FloatField(max_length=5)
    Mn=models.FloatField(max_length=5)
    B=models.FloatField(max_length=5)
