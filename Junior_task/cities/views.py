from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from cities.forms import CityForm
from cities.models import City

__all__ = (
    'home',
    'CityDetailView',
    'CityCreateView',
    'CityUpdateView',
    'CityDeleteView',
    'CityListView'
)


def home(request):

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

    all_cities = City.objects.all()

    paginator = Paginator(all_cities, 3)
    page_number = request.GET.get('page')
    cities = paginator.get_page(page_number)

    context = {
        'page_obj': cities,
        'form': CityForm,
    }

    return render(request, 'cities/home.html', context=context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'

    success_url = reverse_lazy('cities:home')
    success_message = 'Город успешно создан.'


class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'

    success_url = reverse_lazy('cities:home')
    success_message = 'Город успешно изменен.'


class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    # template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Город успешно удален')
        return self.post(request, *args, **kwargs)


class CityListView(ListView):

    paginate_by = 3
    model = City
    template_name = 'cities/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        form = CityForm
        context['form'] = form

        return context
