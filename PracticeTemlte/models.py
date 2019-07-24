from django.db import models

class TravelPlaces(models.Model):
    
    location= models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.TextField()
    img=models.ImageField(upload_to="pics")
    offer=models.BooleanField(default=False)
# Create your models here.
