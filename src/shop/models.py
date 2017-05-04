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
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, db_index=True, null=True, unique=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    engine_power = models.IntegerField(blank=True, null=True)
    car_type = models.PositiveSmallIntegerField(choices=CAR_TYPES)
    publication_date = models.DateField(null=True)
    class Meta:
        """Сортировка по дате.За кастомные названия отвечает verbose_name."""
        ordering = ['publication_date']
        verbose_name = 'car list'
        verbose_name_plural = 'Tesla Car'

    def __str__(self):
        return self.title
