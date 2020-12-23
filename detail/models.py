from django.db import models

# Create your models here.
from lk.models import User


class Hotel(models.Model):
    HotelImg = models.ImageField(blank=True,
                                 null=True,
                                 verbose_name='Фото отеля')

    HotelName = models.CharField(max_length=50,
                                 verbose_name='Название отеля')

    HotelAdress = models.CharField(max_length=50,
                                   verbose_name='Адрес отеля')

    HotelPrice = models.CharField(max_length=30,
                                  verbose_name='Цена отеля: от')
    def __str__(self):
        return self.HotelName
