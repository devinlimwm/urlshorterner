from django.urls import path
from .views import ShortenUrl

urlpatterns = [
    path("goto/<str:short_url>", ShortenUrl().get, name='goto'),
    path("create/", ShortenUrl().post, name='create')
]
