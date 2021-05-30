from django.db import models
from places.fields import PlacesField

class MyLocationModel(models.Model):
    location = PlacesField()
# Create your models here.
