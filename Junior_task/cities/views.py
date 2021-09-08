import requests
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from cities.forms import HtmlForm
from cities.models import City

__all__ = (
    'home',
    'CityDetailView'
)


def home(request, pk=None):
    if request.method == 'POST':
        form = HtmlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

    qs = City.objects.all()
    context = {
        'cities': qs,
        'form': HtmlForm,
    }

    return render(request, 'cities/home.html', context=context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'
