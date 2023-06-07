from django.test import SimpleTestCase
from django.urls import resolve, reverse

from view_app.views import hello_function_view, HelloClassView

# Testowanie w Django:
# - testować urls
# - testować widoku
# - testować modele
# - testować formularze


# Testowanie urls
# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_hello_template_url(self):
        """Testowanie url dla widoku funkcyjnego."""

        url = reverse('view_app:hello_template')
        # print(resolve(url))  # zawiera func, url_name, app_name, namespace, route, args i kwargs

        view = resolve(url).func
        # assert view == hello_function_view
        self.assertEqual(view, hello_function_view)

    def test_hello_template2_url(self):
        """Testowanie url dla widoku klasowego."""

        url = reverse('view_app:hello_template2')
        view = resolve(url).func.view_class

        self.assertEqual(view, HelloClassView)
