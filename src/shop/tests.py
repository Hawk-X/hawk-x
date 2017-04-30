from django.test import TestCase, Client


class ShopStatusTest(TestCase):
    def shop_page(self):
        c = Client()
        response = c.get("/shop")
        self.assertEquals(response.status_code, 200)
