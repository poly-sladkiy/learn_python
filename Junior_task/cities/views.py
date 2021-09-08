from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from cities.models import City

__all__ = (
    'home',
    'CityDetailView'
)


def home(request, pk=None):
    # if pk:
    # city = City.objects.filter(pk=pk).first()
    # city = City.objects.get(pk=pk)
    # city = get_object_or_404(City, pk=pk)
    #
    # context = {'city': city}
    # return render(request, 'cities/detail.html', context)

    qs = City.objects.all()
    context = {'cities': qs}

    return render(request, 'cities/home.html', context=context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'
