from django.test import TestCase, Client


from .models import Contact


class PageTest(TestCase):
	"""Простой тест вьюхи"""
	def home_page(self):
		c = Client()
		response = c.get("/")
		self.assertEquals(response.status_code, 200)


class ContactTest(TestCase):
	def setUp(self):
		Contact.objects.create(first_name="Dennis", question="UNIX is basically a simple operating system")
		Contact.objects.create(last_name="Ritchie", question="but you have to be a genius to understand the simplicity")

	def test_speak(self):
		Dennis = Contact.objects.get(first_name="Dennis")
		Ritchie = Contact.objects.get(last_name="Ritchie")
		# self.assertEquals(Dennis.(), 'The Dennis says "UNIX is basically a simple operating system"')
		# self.assertEquals(Dennis.speak(), 'The Ritchie says "but you have to be a genius to understand the simplicity"')