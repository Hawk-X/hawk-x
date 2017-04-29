#!/usr/bin/python
from django import forms

# Local model Shop application
from .models import TeslaCar


class TeslaForm(forms.ModelForm):
    class Meta:
        model = TeslaCar
        fields = ('title', 'author', 'price', 'car_type', 'engine_power', 'publication_date')