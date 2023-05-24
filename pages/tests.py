from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
# Create your tests here.
from .views import HomePageView

class HomePageViewTest(SimpleTestCase):

    def setUp(self):
        url = reverse('homepage')
        self.res = self.client.get(url)

    def test_status_code(self):
        self.assertEqual(self.res.status_code, 200)

    def test_correct_template(self):
        self.assertTemplateUsed(self.res, 'home.html')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )
