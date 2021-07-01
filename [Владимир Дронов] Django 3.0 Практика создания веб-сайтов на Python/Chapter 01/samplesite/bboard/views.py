from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse, FileResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse

from .models import Bb, Rubric
from .forms import BbForm


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