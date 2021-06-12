from django.db import models
from django.contrib.auth.models import User


class Measure(models.Model):
    class Measurements(float, models.Choices):
        METERS = 1.0, 'Метры'
        FEET = 0.3048, 'Фунты'
        YARDS = 0.9144, 'Ярды'

    measurement = models.FloatField(choices=Measurements.choices)


class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Spare(models.Model):
    name = models.CharField(max_length=50)


class Machine(models.Model):
    name = models.CharField(max_length=30)
    spares = models.ManyToManyField(Spare)


class Bb(models.Model):
    # Создание полей со списком
    class Kinds(models.TextChoices):
        """
        Способен хранить значение из ограниченного набора, заданного в особом перечне
        """
        BUY = 'b', 'Куплю'
        SELL = 's', 'Продам'
        EXCHANGE = 'c', 'Обменяю'
        RENT = 'r'

        __empty__ = 'Выберете тип публикуемого объявления'

    kind = models.CharField(max_length=1, choices=Kinds.choices, default=Kinds.SELL)

    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    rubric = models.ForeignKey('Rubric', null=True,
                               on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'

        ''' Cannot be together '''
        # ordering = ['-published']
        order_with_respect_to = 'rubric'

        unique_together = (
            ('title', 'published'),
            ('title', 'price', 'rubric'),
        )

        get_latest_by = '-published'

        indexes = [
            models.Index(fields=['-published', 'title'],
                         name='bb_partial',
                         condition=models.Q(price__lte=10000))
        ]


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True,
                            verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
