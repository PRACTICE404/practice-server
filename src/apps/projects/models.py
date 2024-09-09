from django.db import models

from apps.base.models import Record
from apps.customers.models import Customer


class Project(Record, models.Model):
    title = models.CharField(max_length=128)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
