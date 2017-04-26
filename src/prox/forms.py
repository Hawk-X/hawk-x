#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms

# Local Model
from .models import Contact


class ContactForm(forms.ModelForm):
	"""Простая форма с полями.
	Добавляется во вьюху и не только.
	Может быть созданна прямо во вьюхе."""
	class Meta:
		model = Contact
		fields = ['first_name', 'last_name', 'email', 'phone', 'question']
