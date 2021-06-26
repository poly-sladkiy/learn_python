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
    # edited = models.DateTimeField(verbose_name='Изменено')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    rubric = models.ForeignKey('Rubric', null=True,
                               on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        # Название набора сущностей
        verbose_name_plural = 'Объявления'

        # Название самой сущности
        verbose_name = 'Объявление'

        # параметры сортировки
        ordering = ['-published', 'title']

        # Позволяет сделать модель записей произвольно упорядочиваемым
        # order_with_respect_to = 'rubric'

        # Последовательность имен, которое должно быть уникальным в пределах таблицы
        unique_together = (
            ('title', 'published'),
            ('title', 'price', 'rubric'),
        )

        # Имя поля типа DateField / DateTimeField
        # которое будет возвращать latest / earliest по данному правилу
        get_latest_by = ['edited', 'published']

        """
            Последовательность индексов, включающих в себя несколько полей
            
            !!! MySQL и MarinaDB не поддерживают condition и будут игнорировать это
        """
        indexes = [
            models.Index(fields=['-published', 'title'],  # поля для включения в индекс
                         name='%(app_label)s_%(class)s_partial',  # Имя индеса
                         condition=models.Q(price__lte=10000)),  # Критерий, которому должно удовлетворять

            models.Index(fields=['title', 'price', 'rubric']),
        ]

        # Другой способ задания индексов
        # index_together = [
        #     ['-published', 'title'],
        #     ['title', 'price', 'rubric']
        # ]

        # Условия, которым должны удовлетворять значения, заносимые в поля
        '''        
        constraints = (
            # Критерий для занесения в БД
            models.CheckConstraint(
                check=models.Q(price__gte=0) & \
                      models.Q(price__lte=1000000),
                name='bboard_rubric_price_constraint'  # Или '%(app_label)s_%(class)s_price_constraint'
            ),

            # Поля с уникальными значениями
            models.UniqueConstraint(
                fields=('title', 'price'),
                name='%(app_label)s_%(class)s_title_price_constraint'
            ),

        )
        '''


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True,
                            verbose_name='Название')

    # Императивный метод интернет адресс модели
    def get_absolute_url(self):
        return "/bboard/%s/" % self.pk

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
