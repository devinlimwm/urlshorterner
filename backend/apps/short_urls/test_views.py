from django.test import TestCase, RequestFactory
from django.http import Http404
from .views import ShortUrlView
from .models import Url
from unittest.mock import MagicMock, patch


class ViewTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_get_short_url_from_db_exists(self):
        Url.objects.create(
            short_url='1234', long_url='https://www.google.com', visits=0)
        request = self.factory.get('/goto/1234')
        view = ShortUrlView()
        view.setup(request)

        response = view.get(request=request, short_url="1234")

        self.assertEqual(response.status_code, 302)

    def test_get_short_url_from_db_not_exists(self):
        request = self.factory.get('/goto/1234')
        view = ShortUrlView()
        view.setup(request)

        with self.assertRaises(Http404):
            view.get(request=request, short_url="1234")

    def test_get_short_url_from_db_save_fails(self):
        Url.objects.create(
            short_url='12345', long_url='https://www.google.com', visits=0)
        request = self.factory.get('/goto/1234')
        view = ShortUrlView()
        view.setup(request)

        Url.save = MagicMock(side_effect=ValueError)

        response = view.get(request=request, short_url="12345")

        self.assertEqual(response.status_code, 500)

    def test_create_short_url_success(self):
        request = self.factory.post('/short/url')
        request.POST._mutable = True
        request.POST.update({"long_url": "https://www.google.com"})
        view = ShortUrlView()
        view.setup(request)

        response = view.post(request=request)

        self.assertEqual(response.status_code, 200)

    def test_create_short_url_not_found(self):
        request = self.factory.post('/short/url')
        request.POST._mutable = True
        request.POST.update({"long_url": ""})
        view = ShortUrlView()
        view.setup(request)

        response = view.post(request=request)

        self.assertEqual(response.status_code, 400)

    def test_create_short_url_not_fully_formed(self):
        request = self.factory.post('/short/url')
        request.POST._mutable = True
        request.POST.update({"long_url": "asd.com"})
        view = ShortUrlView()
        view.setup(request)

        response = view.post(request=request)

        self.assertEqual(response.status_code, 400)

    @patch('apps.short_urls.models.Url.save', MagicMock(side_effect=ValueError))
    def test_create_short_url_save_fail(self):
        request = self.factory.post('/short/url')
        request.POST._mutable = True
        request.POST.update({"long_url": "https://www.google.com"})
        view = ShortUrlView()
        view.setup(request)

        response = view.post(request=request)

        self.assertEqual(response.status_code, 500)
