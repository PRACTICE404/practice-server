from django.db import models

from apps.base.models import Record


class Customer(Record):
    nickname = models.CharField(max_length=64)

    def __str__(self):
        return self.nickname
