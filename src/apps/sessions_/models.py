from django.core.exceptions import ValidationError
from django.db import models

from apps.base.models import Record
from apps.orders.models import Task


class Session(Record):
    date = models.DateField()
    obsidian_id = models.PositiveIntegerField()
    minutes_working = models.PositiveIntegerField()
    document = models.FileField(upload_to='sessions/session/document/', blank=True, null=True)  # NOQA

    def __str__(self):
        return f"{self.date} {self.minutes_working}"


class SessionDistribution(Record):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='session_distributions'
    )
    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        related_name='distributions'
    )
    minutes = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.task} (self.minutes)"

    def clean_fields(self, exclude=None):
        if (self.session.distributions.exclude(id=self.id).aggregate(models.Sum('minutes'))['minutes__sum'] or 0) + self.minutes > self.session.minutes_working:  # NOQA
            raise ValidationError({
                'minutes': 'More than possible is distributed!',
            })

    class Meta:
        verbose_name_plural = 'Session distribution'
