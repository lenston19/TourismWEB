from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q
from .models import Hotel

# Create your views here.

class HotelView(ListView):
    model = Hotel
    template_name = 'detail/detailinfo.html'
    context_object_name = 'hotels'

class SearchResultsView(ListView):
    model = Hotel
    template_name = 'detail/searchhotel.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = Hotel.objects.filter(
            Q(HotelName__icontains=query)
        )
        return object_list