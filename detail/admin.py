from django.contrib import admin

from .models import Hotel

# Register your models here.


class HotelAdmin(admin.ModelAdmin):
    list_display = ('HotelName','HotelAdress','HotelPrice')
    list_filter = ('HotelPrice', )

admin.site.register(Hotel, HotelAdmin)
Hotel.objects.filter(HotelPrice='3200')