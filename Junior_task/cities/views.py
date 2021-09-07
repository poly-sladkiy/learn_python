from django.shortcuts import render

from cities.models import City

__all__ = (
    'home',
)


def home(request):
    qs = City.objects.all()
    context = {'cities': qs}

    return render(request, 'cities/home.html', context=context)
