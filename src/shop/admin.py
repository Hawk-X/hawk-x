from django.contrib import admin

# Local Model.py
from .models import TeslaCar


class TeslaAdmin(admin.ModelAdmin):
    """Вывод список по описанию, цене и мощности.Фильтр по типу машины.Поиск по описанию, типу и цене."""
    list_display = ['title', 'price', 'engine_power']
    list_filter = ['car_type']
    search_fields = ['title', 'car_type', 'price']
    class Meta:
        model = TeslaCar

admin.site.register(TeslaCar, TeslaAdmin)
