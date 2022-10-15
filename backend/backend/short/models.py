from django.db import models


class Url(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    short_url = models.CharField(max_length=10)
    long_url = models.CharField(max_length=256)
    visits = models.IntegerField()

    def __str__(self):
        return self.long_url + self.short_url + created_at

    class Meta:
        ordering = ['-visits']
