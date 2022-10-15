from django.db import models
from backend.short.services import UuidService


class Url(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    short_url = models.CharField(
        primary_key=True, unique=True, default=UuidService.shortUuid, max_length=10)
    long_url = models.CharField(max_length=256)
    visits = models.IntegerField(default=0)

    def __str__(self):
        return self.long_url + self.short_url + self.created_at

    class Meta:
        ordering = ['-visits']
