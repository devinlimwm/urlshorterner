from django.urls import path
from .views import ShortUrlView

urlpatterns = [
    path("goto/<str:short_url>", ShortUrlView().get, name='goto'),
    path("short/url", ShortUrlView().post, name='shorten_url')
]
