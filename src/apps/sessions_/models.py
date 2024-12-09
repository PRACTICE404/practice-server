from django.core.exceptions import ValidationError
from django.db import models

from apps.base.models import Record
from apps.orders.models import Task


class Session(Record):
    date = models.DateField()
    minutes_working = models.PositiveIntegerField()
    datetime_start = models.DateTimeField(auto_now_add=True)
    datetime_end = models.DateTimeField(blank=True, null=True)
    obsidian_id = models.PositiveIntegerField(blank=True, null=True)
    document = models.FileField(
        upload_to='sessions/session/document/',
        blank=True,
        null=True
    )

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
    minutes = models.PositiveIntegerField(
        help_text='Sum of minutes in session have to be equal to it\'s minutes'
    )

    def __str__(self):
        return f"{self.task} (self.minutes)"

    def clean_fields(self, exclude=None):
        if (self.session.distributions.exclude(id=self.id).aggregate(models.Sum('minutes'))['minutes__sum'] or 0) + self.minutes > self.session.minutes_working:  # NOQA
            raise ValidationError({
                'minutes': 'More than possible is distributed!',
            })

    class Meta:
        verbose_name_plural = 'Session distribution'


class SessionSignal(Record):
    CHOICES_TYPE = (
        ('start', 'Start'),
        ('finish', 'Finish'),
        ('regular', 'Regular'),
        ('break_start', 'Break start'),
        ('break_end', 'Break end')
    )
    content = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=12, choices=CHOICES_TYPE)

    session = models.ForeignKey(
        to=Session,
        on_delete=models.CASCADE,
        related_name='signals'
    )

    class Meta:
        ordering = ['-id']

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        if not self.type == 'break_end' and not self.content:
            raise ValidationError('Content is required if type is not "Break end"')  # noqa
        if signal_last := self.session.signals.first():
            if signal_last.type == 'break_start' and not self.type == 'break_end':  # noqa
                raise ValidationError('You have to stop break!')  # noqa
            if signal_last.type == 'finish':  # noqa
                raise ValidationError('Cannot create signal for finished session!')  # noqa    
        else:
            if not self.type == 'start':
                print(self.type)
                raise ValidationError('You have to create start signal first!')

    def __str__(self):
        return f'Session signal ({self.id}): {self.created}'
