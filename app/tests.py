from django.test import TestCase
from django.core import reverse
# Create your tests here.
class TestHomePage(TestCase):
    def test_home(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)
