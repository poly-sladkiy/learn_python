from django import forms

from cities.models import City


class HtmlForm(forms.Form):
    name = forms.CharField(max_length=50, label='Город')


class CityForm(forms.ModelForm):

    name = forms.CharField(
        label='Город',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название города',
        })
    )

    class Meta:
        model = City
        fields = ('name',)
