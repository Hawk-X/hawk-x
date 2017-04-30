from django.test import TestCase, Client


class PageTest(TestCase):
    """Простой тест вьюхи"""

    def home_page(self):
        c = Client()
        response = c.get("/")
        self.assertEquals(response.status_code, 200)
