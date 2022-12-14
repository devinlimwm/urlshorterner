from django.db import models
from .services import UuidService


class Url(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    short_url = models.CharField(
        primary_key=True, unique=True, default=UuidService.short_uuid, max_length=10)
    long_url = models.CharField(max_length=256)
    visits = models.IntegerField(default=0)

    def __str__(self):
        return f'long: {self.long_url} short: {self.short_url} visits: {self.visits}'

    class Meta:
        ordering = ['-visits']
