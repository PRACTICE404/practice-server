from django.db import models

from apps.base.models import Record


class ProgrammingLanguage(Record):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class TechnologyArea(Record):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Technology(Record):
    name = models.CharField(max_length=32)
    programming_language = models.ForeignKey(
        ProgrammingLanguage,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='technologies'
    )
    area = models.ForeignKey(
        TechnologyArea,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='technologies'
    )

    def __str__(self):
        return f'{self.programming_language or ""} {self.name}'

    def pre_save(self):
        print('post_save')

    class Meta:
        verbose_name_plural = 'Technologies'
        ordering = ('programming_language__name', 'name')


class Service(Record):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    technology_areas = models.ManyToManyField(TechnologyArea, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = (
            '-is_active',
            'title'
        )


class Portfolio(Record):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.service} {self.title}'

    class Meta:
        verbose_name_plural = 'Portfolio'
        ordering = (
            'is_finished',
        )


class Faq(Record):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    text_question = models.TextField()
    text_answer = models.TextField()

    def __str__(self):
        return f'{self.text_question} {self.text_answer}'

    class Meta:
        verbose_name_plural = 'FAQ'
