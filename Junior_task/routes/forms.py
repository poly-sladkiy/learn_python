from django import forms

from cities.models import City


class RouteForm(forms.Form):

    from_city = forms.ModelChoiceField(
        label='Готод отправления',
        queryset=City.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )

    to_city = forms.ModelChoiceField(
        label='Готод прибытия',
        queryset=City.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )

    cities = forms.ModelMultipleChoiceField(
        label='Через города',
        queryset=City.objects.all(),
        required=False,
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control',
            }
        )
    )

    travelling_time = forms.IntegerField(
        label='Время в пути',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Время в пути',
        })
    )
