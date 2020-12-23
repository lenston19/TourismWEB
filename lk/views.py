
from django.views.generic.list import ListView
from django.shortcuts import render
from detail.models import Hotel
from detail.views import SearchResultsView
from lk.forms import RegistrationForm

# def lk(request):
#     return render(request, 'lk/lk.html')

def SignUp(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/login.html', {})
    else:
        form = RegistrationForm()
        return render(request, 'lk/registr.html', {'form': form})

class lk(ListView):
    model = Hotel
    template_name = 'lk/lk.html'
    paginate_by = 3

    def get_queryset(self):  # новый
        HotelName = self.kwargs.get("HotelName")
        if HotelName:
            object_list = Hotel.objects.filter(HotelName__icontains=HotelName)
        else:
            object_list = Hotel.objects.all()
        return object_list