from django.db import models

from apps.base.models import Record
from apps.projects.models import Project


class Order(Record):
    STATUS_CHOICES = (
        ('1', 'active'),
        ('2', 'pending'),
        ('3', 'finished'),
        ('4', 'canceled')
    )

    title = models.CharField(max_length=64)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default='2')  # NOQA

    class Meta:
        verbose_name_plural = '(A) Orders'

    @property
    def estimate(self):
        return self.epics.aggregate(models.Sum('tasks__estimate'))['tasks__estimate__sum']  # NOQA

    def __str__(self):
        return f"{self.project.title} >> {self.title}"


class OrderHistory(Record):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name='histories')  # NOQA
    text = models.TextField()

    class Meta:
        verbose_name_plural = '(D) Histories'

    def __str__(self):
        return f'{self.order} > {self.text}'


class Epic(Record):
    title = models.CharField(max_length=64)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name='epics')  # NOQA

    class Meta:
        verbose_name_plural = '(B) Epics'

    @property
    def estimate(self):
        return self.tasks.aggregate(models.Sum('estimate'))['estimate__sum']

    def __str__(self):
        return f"{self.order} >> {self.title}"


class Task(Record):
    CHOICES_STATUS = (
        ('ready', 'Ready'),
        ('pending', 'Pending'),
        ('in_progress', 'In progress'),
        ('done', 'Done')
    )

    title = models.CharField(max_length=128)
    epic = models.ForeignKey(to=Epic, on_delete=models.CASCADE, related_name='tasks')  # NOQA
    status = models.CharField(max_length=24, choices=CHOICES_STATUS)
    is_backlog = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    estimate = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = '(C) Tasks'

    def __str__(self):
        return self.title
