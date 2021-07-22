from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms import modelformset_factory
from django.forms.formsets import ORDERING_FIELD_NAME
from django.shortcuts import redirect, render

from .models import Bb, Rubric


def rubric(request):
    RubricFormSet = modelformset_factory(Rubric, fields=('name',),
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


class BbForm(forms.ModelForm):
    title = forms.CharField(label='Название товара',
                            validators=[validators.RegexValidator(r'^.{4,}$')],
                            error_messages={'invalid': 'Слишком короткое название товара.'})
    content = forms.CharField(label='Описание',
                              widget=forms.widgets.Textarea())
    price = forms.DecimalField(label='Цена', decimal_places=2)
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),
                                    label='Рубрика',
                                    help_text='Не забудьте ввести рубрику!',
                                    widget=forms.widgets.Select(attrs={'size': 2}))
    '''
    forms.widgets.Select принимает словарь attr,
    в котором можно указать значение size, если его не передавать,
    то вывод будет как обычной качелькой
    '''

    def clean_title(self):
        val = self.cleaned_data['title']
        if val == 'Прошлогодний снег':
            raise ValidationError('К продаже не допускается')
        return val

    def clean(self):
        super().clean()
        errors = {}

        if not self.cleaned_data['content']:
            errors['content'] = ValidationError(
                'Укажите описание продаваемого товара!')
        if self.cleaned_data['price'] < 0:
            errors['price'] = ValidationError(
                'Укажите неотрицательное значение цены!')

        if errors:
            raise ValidationError(errors)

    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')
