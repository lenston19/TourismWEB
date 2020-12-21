from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from lk.forms import RegistrationForm
# Create your views here.

def lk(request):
    return render(request, 'lk/lk.html')

def SignUp(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/login.html', {})
    else:
        form = RegistrationForm()
        return render(request, 'lk/registr.html', {'form': form})
