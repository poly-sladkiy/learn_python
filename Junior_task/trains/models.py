from django.db import models

from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Номер поезда')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Время в пути')

    from_city = models.ForeignKey(City,
                                  on_delete=models.CASCADE,
                                  related_name='from_city_set',
                                  verbose_name='Город отправления')

    to_city = models.ForeignKey('cities.City',
                                on_delete=models.CASCADE,
                                related_name='to_city_set',
                                verbose_name='Город прибытия')

    def __str__(self):
        return f'Поезд № {self.name} из {self.from_city} в {self.to_city} время отправления {self.travel_time}'

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['name',]