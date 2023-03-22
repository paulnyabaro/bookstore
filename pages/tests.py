from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    # def test_homepage_url_name(self):
    #     self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'home page')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'This is not on the page')