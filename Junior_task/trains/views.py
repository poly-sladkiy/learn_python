from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from trains.forms import TrainForm
from trains.models import Train

__all__ = (
    'home',
    'TrainListView',
    'TrainDetailView',
    'TrainCreateView',
    'TrainUpdateView',
    'TrainDeleteView',
)


def home(request):
    all_cities = Train.objects.all()

    paginator = Paginator(all_cities, 5)
    page_number = request.GET.get('page')
    trains = paginator.get_page(page_number)

    context = {
        'page_obj': trains,
    }

    return render(request, 'trains/home.html', context=context)


class TrainListView(ListView):
    paginate_by = 5
    model = Train
    template_name = 'trains/home.html'


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'


class TrainCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'

    success_url = reverse_lazy('trains:home')
    success_message = 'Поезд успешно создан.'


class TrainUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'

    success_url = reverse_lazy('trains:home')
    success_message = 'Поезд успешно изменен.'


class TrainDeleteView(LoginRequiredMixin, DeleteView):
    model = Train
    # template_name = 'trains/delete.html'
    success_url = reverse_lazy('trains:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Город успешно удален')
        return self.post(request, *args, **kwargs)
