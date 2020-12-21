from django.db import models
# Create your models here.

class User(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name=''
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name=''
    )
    email = models.CharField(
        max_length=50,
        verbose_name='',
        unique=True,
    )
    username = models.CharField(
        max_length=50,
        verbose_name='',
        unique=True,
    )

    def __str__(self):
        return f"{self.first_name + self.last_name}"

