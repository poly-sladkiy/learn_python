from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from .models import Bb, Rubric


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
