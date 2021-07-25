from django.db import models

class Product_model(models.Model):
    Product_id=models.IntegerField(primary_key=True)
    Product_Name=models.CharField(null=True,max_length=100)
    Product_Price=models.FloatField()
    Product_Image=models.FileField()

