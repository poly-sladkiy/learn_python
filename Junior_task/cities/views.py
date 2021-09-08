from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from cities.forms import CityForm
from cities.models import City

__all__ = (
    'home',
    'CityDetailView',
    'CityCreateView',
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


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'

    success_url = reverse_lazy('cities:home')
