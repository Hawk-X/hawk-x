from django.db import models


class Contact(models.Model):
	"""Стандартная модель для обратной связи"""
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=30)
	email = models.EmailField()
	phone = models.CharField(max_length=25)
	question = models.TextField(max_length=200)
	created = models.DateField(null=True)
	class Meta:
		"""Сортировка по дате созданию. Свежие записи вверху.
		За кастомные названия отвечает verbose_name."""
		ordering = ['created']
		verbose_name='cписок'
		verbose_name_plural='Обратная связь'

	def __str__(self):
		return self.question