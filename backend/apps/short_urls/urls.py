from django.urls import path
from .views import ShortUrlView

urlpatterns = [
    path("short/url/<str:short_url>", ShortUrlView().get, name='get_long_url'),
    path("short/url", ShortUrlView().post, name='shorten_url')
]
