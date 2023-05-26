from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
# Create your tests here.
from .views import HomePageView, AboutPageView

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


class AboutPageViewTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_correctTemplateUsed(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_contain(self):
        self.assertContains(self.response, "About page")
    
    def test_not_contains(self):
        self.assertNotContains(self.response, "I shouldn't be here!")
        
    def test_about_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )