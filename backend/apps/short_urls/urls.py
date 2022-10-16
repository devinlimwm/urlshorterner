from django.urls import path
from .views import ShortUrlView

urlpatterns = [
    path("goto/<str:short_url>", ShortUrlView().get, name='goto'),
    path("create/", ShortUrlView().post, name='create')
]
