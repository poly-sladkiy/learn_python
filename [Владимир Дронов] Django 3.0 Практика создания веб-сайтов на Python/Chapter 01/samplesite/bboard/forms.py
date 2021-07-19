from django import forms

from .models import Bb, Rubric


class BbForm(forms.ModelForm):
    title = forms.CharField(label='Название товара')
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

    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')
