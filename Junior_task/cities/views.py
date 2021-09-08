import requests
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from cities.forms import CityForm
from cities.models import City

__all__ = (
    'home',
    'CityDetailView'
)


def home(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

    qs = City.objects.all()
    context = {
        'cities': qs,
        'form': CityForm,
    }

    return render(request, 'cities/home.html', context=context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'
