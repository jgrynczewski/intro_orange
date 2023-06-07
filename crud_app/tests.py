from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve

from crud_app.views import task_detail_view
from crud_app.models import Task


# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_task_detail_view_url(self):
        """Test sparametryzowanego url."""

        url = reverse('crud_app:task_detail_view', args=[3])
        view = resolve(url).func

        self.assertEqual(view, task_detail_view)


class TestViews(TestCase):
    def setUp(self):
        """Ta metoda zostanie uruchomiona przed każdym testem w tej klasie."""

        self.task = Task.objects.create(name='Pisanie')
        self.task_list_view_url = reverse('crud_app:task_list_view')
        self.task_detail_view_url = reverse('crud_app:task_detail_view', args=[1])

    def test_task_list_view(self):
        response = self.client.get(self.task_list_view_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crud_app/task_list.html')

        content = str(response.content)
        self.assertIn("Lista", content)

    def test_task_detail_view(self):
        response = self.client.get(self.task_detail_view_url)

        # Testowanie statusu odpowiedzi
        self.assertEqual(response.status_code, 200)

        # Testowanie wyświetlanego szablonu
        self.assertTemplateUsed(response, 'crud_app/task_detail.html')

        context = response.context
        task = context.get('task')

        # Testowanie szablonu wyświetlanego szablonu
        self.assertIsInstance(task, Task)
        self.assertEqual(task.name, 'Pisanie')
