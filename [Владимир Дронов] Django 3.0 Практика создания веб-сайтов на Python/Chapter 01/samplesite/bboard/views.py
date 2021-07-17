from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Bb, Rubric
from .forms import BbForm


class BbDetailView(DetailView):
    """
    Класс выводящий одну запись.

    Ищет запись по полученным значениям ключа или слага, заносит в атрибут object
    и выводит на экран страницу с содержимым этой записи.
    """
    model = Bb

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()

        return context


class BbByRubricView(TemplateView):
    template_name = 'bboard/by_rubric.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bbs'] = Bb.objects.filter(rubric=context['rubric_id'])
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=context['rubric_id'])

        return context


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('bboard:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


def index(request):
    data = {
        'title': 'Мотоцикл',
        'content': 'Страрый',
        'price': 10000.0
    }

    return JsonResponse(data)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    currunt_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'bbs': bbs,
        'rubrics': rubrics,
        'current_rubric': currunt_rubric,
    }

    return render(request, 'bboard/by_rubric.html', context)