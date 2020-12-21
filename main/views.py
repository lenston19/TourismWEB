from django.shortcuts import render

from django.utils import timezone
# Create your views here.
from django.template.context_processors import csrf

from main.forms import DateRangeForm


def home(request):
    if request.method == "POST":
        f = DateRangeForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.end_date = timezone.now()
            c.save()
    else:
        f = DateRangeForm()
        args = {}
        args.update(csrf(request))
        args['form'] = f

    return render(request, 'main/index.html', {
        'form': f
    })
