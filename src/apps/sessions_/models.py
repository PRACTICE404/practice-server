from django.db import models

from apps.base.models import Record


class Session(Record):
    date = models.DateField()
    obsidian_id = models.PositiveIntegerField()
    minutes_working = models.PositiveIntegerField()
    document = models.FileField(upload_to='sessions/session/document/', blank=True, null=True)  # NOQA

    def __str__(self):
        return f"{self.date} {self.minutes_working}"
