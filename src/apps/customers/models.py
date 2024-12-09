from django.db import models

from apps.base.models import Record


class Customer(Record):
    CHOICES_CHANNEL = (
        ('kwork', 'Kwork'),
        ('upwork', 'Upwork'),
        ('facebook', 'Facebook'),
        ('threads', 'Threads')
    )

    nickname = models.CharField(max_length=64)
    full_name = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    channel = models.CharField(
        max_length=24,
        choices=CHOICES_CHANNEL,
        blank=True,
        null=True
    )

    respectfull_communication = models.BooleanField(default=False)
    note = models.TextField(blank=True, null=True)

    telegram_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nickname
