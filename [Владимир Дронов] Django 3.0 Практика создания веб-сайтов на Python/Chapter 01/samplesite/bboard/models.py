from django.db import models
from django.core import validators
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Собственный валидатор - функция
# Необходимо, чтобы функия принимала только
# 1 аргумент - число которое нужно проверить
# в случае провала - вызвать исключение
def validate_even(val):
    """
    Если число не является четным, то
    вызывается исключение ValidationError

    - 1 аргумент    - сообщение об ошибке
    - code: str     - код ошибки
    - params: map   - значения, которые нужно поместить
        в сообщении об ошибке.
    """
    if val % 2 != 0:
        raise ValidationError(f'Число {val} нечетное',
                              code='odd',
                              params={'value': val})


# Валидатор класс - нужен для того,
# если необходимо передать какие-то
# параметры задающие работу данного
# валидатора
class MinMaxValueValidator:

    def __init__(self, min_value, max_value):
        """
        Конструктор задает работу валидотора
        """
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, val):
        """
        Принимает одно значение, которое проверяется по
        соответствующим данным
        """
        if val < self.min_value or val > self.max_value:
            raise ValidationError('Введенное число должно '
                                  f'находится в диапазоне от {self.min_value} до {self.max_value}',
                                  code='out_of_range',
                                  params={'min': self.min_value, 'max': self.max_value})


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


def get_min_length():
    # Вычисляем длину
    min_length = 4

    return min_length


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

    title = models.CharField(max_length=50, verbose_name='Товар',
                             validators=[
                                 # Проверка регулярным выражением:
                                 #      - regex - само выражение
                                 #      - message - сообщение об ошибке
                                 #      - code - код ошибки
                                 #      - inverse_match - должно ли НЕ соответсвовать выражению
                                 #      - flag - флаги regex - str
                                 validators.RegexValidator(regex='^.{4,}$'),

                                 # Проверка минимальной длины
                                 #      - message
                                 #      - code
                                 # validators.MinLengthValidator(get_min_length),

                                 # Проверка почты
                                 #      - message
                                 #      - code
                                 # validators.EmailValidator(),

                                 # Проверка введенного url
                                 #      - schemes=None - ['http', 'https', 'ftp', 'ftps']
                                 #      - regex - само выражение - str / regex
                                 #      - message
                                 #      - code
                                 # validators.URLValidator(),

                                 # Проверка значения
                                 # validators.MinValueValidator(<value>),
                                 # validators.MaxValueValidator(<value>),

                                 # Проверяем фиксированную точность
                                 # validators.DecimalValidator(<максимальное кол-во цифр в числе>,
                                 #                             <кол-во цифр в дробной части>),

                                 # Валидаторы в виде функции

                                 # validators.validate_ipv46_address(),
                                 # validators.validate_ipv4_address(),
                                 # validators.validate_ipv6_address(),

                                 # validators.int_list_validator(),
                             ],

                             # Вывод собственных сообщений об ошибках.
                             error_messages={
                                 'invalid': 'Неверное имя товара',
                                 # 'null': 'text',
                                 # 'blank': 'text',
                                 # 'unique': 'text',
                                 # 'invalid_date': 'text',
                                 # 'invalid_time': 'text',
                                 # 'min_length': 'text',
                                 # 'max_length': 'text',
                                 # ...
                             }
                             )

    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена',
                              validators=[validate_even])

    # edited = models.DateTimeField(verbose_name='Изменено')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    rubric = models.ForeignKey('Rubric', null=True,
                               on_delete=models.PROTECT, verbose_name='Рубрика')

    def clean(self):
        """
        Бывают случаи, когда нужно проверить значения всей модели
        для этого применяется переопределение метода clean()

        Метод не должен принимать аргументы или возвращать результат.
        Он должен возбудить исключение, если это требуется.
        """
        errors = {}

        if not self.content:
            errors['content'] = ValidationError('Укажите описание продаваемого товара')
        if self.price and self.price < 0:
            errors['price'] = ValidationError('Укажите неотрицательное значени цены')
        if errors:
            raise ValidationError(errors)



    # Функциональное поле - выполняет вычисления над данными,
    # которые можно только прочитать.
    # Не принимает никаких параметров
    # Вызывается как - {{ bb.title_and_price }}
    def title_and_price(self):
        if self.price:
            return '%s (%.2f)' % (self.title, self.price)
        else:
            return self.title

    # Описание, которое будет выводится на сайте
    title_and_price.short_description = 'Название и цена'

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

    # Возвращает строковое представление записи модели
    # оно будет выводиться при данном вызове - {{ rubric }}
    def __str__(self):
        return self.name

    # Сохраняем запись
    def save(self, *args, **kwargs):
        # Какие-то действия перед сохранением

        # Сохранение
        super().save(*args, **kwargs)
        # Действия после сохранения

        '''
        # Сохраняем, если is_model_correct вернёт True
        # метод необходимо реализовать
        if self.is_model_correct():
            super().save(*args, **kwargs)
            
         '''

    # Удаляем запись
    def delete(self, *args, **kwargs):
        # Какие-то действия перед удалением

        # Удаляем
        super().delete(*args, **kwargs)
        # Действия после удаления

        '''
        # Удаляем, если is_model_correct вернёт True
        # метод необходимо реализовать
        if self.is_model_correct():
            super().delete(*args, **kwargs)

         '''

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
