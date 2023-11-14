from django.db import models
from django.conf import settings


class Census(models.Model):
    name = models.CharField(max_length=200)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    has_voted = models.BooleanField(default=False)

    def __str__(self):
        return self.name    


class Votation(models.Model):
    census = models.ForeignKey(Census, on_delete=models.CASCADE)
