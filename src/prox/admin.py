from django.contrib import admin

# Local Model.py
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
	"""Выводит название по first name, email and phone.
	Фильтрует по дате создания.
	Поиск по first, last name's and email."""
	list_display = ['first_name', 'email', 'phone', 'created']
	list_filter = ['phone','created']
	search_fields = ['first_name', 'last_name', 'email']
	class Meta:
		model = Contact

admin.site.register(Contact, ContactAdmin)		