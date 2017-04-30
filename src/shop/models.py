from django.db import models


class TeslaCar(models.Model):
    """Простая модель Тесла."""
    MODELS = 1
    MODEL3 = 2
    MODELX = 3
    CAR_TYPES = (
        (MODELS, 'Model S'),
        (MODEL3, 'Model 3'),
        (MODELX, 'Model X'),
    )

    title = models.CharField(max_length=50)
    author = models.CharField(blank=True, max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    engine_power = models.IntegerField(blank=True, null=True)
    car_type = models.PositiveSmallIntegerField(choices=CAR_TYPES)
    publication_date = models.DateField(null=True)
    class Meta:
        """Сортировка описанию.За кастомные названия отвечает verbose_name."""
        ordering = ['title']
        verbose_name = 'car list'
        verbose_name_plural = 'Tesla Car'

    def __str__(self):
        return self.title
