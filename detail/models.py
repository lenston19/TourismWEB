from django.db import models

# Create your models here.

class Hotel(models.Model):
    HotelName = models.CharField(max_length=50)
    HotelAdress = models.CharField(max_length=50)
    HotelPrice = models.CharField(max_length=30)

    def __str__(self):
        return self.HotelName
