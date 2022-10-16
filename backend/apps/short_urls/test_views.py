from django.test import TestCase, RequestFactory
from django.http import Http404
from .views import ShortUrlView
from .models import Url
from unittest.mock import MagicMock


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
            short_url='1234', long_url='https://www.google.com', visits=0)
        request = self.factory.get('/goto/1234')
        view = ShortUrlView()
        view.setup(request)

        Url.save = MagicMock(side_effect=ValueError)

        response = view.get(request=request, short_url="1234")

        self.assertEqual(response.status_code, 500)
