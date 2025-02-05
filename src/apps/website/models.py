from django.db import models

from core.models import SingletonModel


class Stats(SingletonModel):
    years = models.PositiveIntegerField()
    projects = models.PositiveIntegerField()
    customers = models.PositiveIntegerField()


class WebsiteSettings(SingletonModel):
    consultation_price = models.PositiveIntegerField(blank=True, null=True)
    slogan = models.TextField()
    location = models.TextField()
