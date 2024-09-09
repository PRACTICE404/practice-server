from django.db import models

from apps.base.models import Record


class Customer(Record, models.Model):
    nickname = models.CharField(max_length=64)
