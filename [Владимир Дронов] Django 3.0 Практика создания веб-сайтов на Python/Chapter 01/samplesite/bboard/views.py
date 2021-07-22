from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import redirect_to_login
from django.core.paginator import Paginator
from django.forms import modelformset_factory
from django.forms.formsets import ORDERING_FIELD_NAME
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.urls import reverse

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


class BbByRubricView(SingleObjectMixin, ListView):
    """
    !!! По мнению автора лучше избегать смешанной функциональности.
    Удобнее взять за основу более низкоуровневый контроллер-класс.
    """
    template_name = 'bboard/by_rubric.html'
    pk_url_kwarg = 'rubric_id'  # URL параметр через который передается ключ рубрики.

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Rubric.objects.all())
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.bb_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = self.object
        context['bbs'] = context['object_list']

        return context


class BbCreateView(FormView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    initial = {'price': 0.0}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def get_success_url(self):
        return reverse('bboard:by_rubric',
                       kwargs={'rubric_id': self.object.cleaned_data['rubric'].pk})


class BbEditView(UpdateView):
    model = Bb
    form_class = BbForm
    template_name = 'bboard/bb_form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()

        return context


class BbDeleteView(DeleteView):
    model = Bb
    success_url = '/'
    template_name = 'bboard/bb_confim_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


def index(request):
    rubrics = Rubric.objects.all()
    bbs = Bb.objects.all()
    paginator = Paginator(bbs, 2)

    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1

    page = paginator.get_page(page_num)
    context = {'rubrics': rubrics, 'bbs': page.object_list, 'page': page}
    return render(request, 'bboard/index.html', context)


'''
    Django decorators (with ex.):
        - @user_passes_test(lambda user: user.is_staff)
        - permission_required(('bboard.view_rubric', 'bboard.add_rubric', ...))
'''

@login_required(login_url='/accounts/login/')
@permission_required(('bboard.add_rubric', 'bboard.delete_rubric',
                      'bboard.change_rubric'))
def rubrics(request):
    RubricFormSet = modelformset_factory(Rubric,
                                         fields=('name',),
                                         can_order=True, can_delete=True)
    if request.method == 'POST':
        formset = RubricFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    rubric = form.save(commit=False)
                    rubric.order = form.cleaned_data[ORDERING_FIELD_NAME]
                    rubric.save()
            return redirect('bboard:index')
    else:
        formset = RubricFormSet()
    context = {'formset': formset}
    return render(request, 'bboard/rubrics.html', context)



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