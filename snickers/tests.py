from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class SnacksTests(SimpleTestCase):
    def test_home_page_status(self):
        self.helper_status_code_200('home')
        # url = reverse('home')
        # response = self.client.get(url)
        # # actual and expected convention also works
        # self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')

    def test_about_page_status(self):
        url = reverse('about')
        response = self.client.get(url)
        # actual and expected convention also works
        self.assertEqual(response.status_code, 200)

    def test_about_page_template(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html')

    def helper_status_code_200(self, url_name):
        url = reverse(url_name)
        response = self.client.get(url)
        # actual and expected convention also works
        self.assertEqual(response.status_code, 200)