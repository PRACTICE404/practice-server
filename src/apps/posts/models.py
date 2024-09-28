from django_summernote.fields import SummernoteTextField

from django.db import models

from apps.base.models import Record


class PostBranch(Record):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Post branches'
        ordering = ('name', )


class PostCategory(Record):
    name = models.CharField(max_length=32)
    branch = models.ForeignKey(
        PostBranch,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('branch__name', 'name')


class PostTag(Record):
    name = models.CharField(max_length=32)
    branch = models.ForeignKey(
        PostBranch,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('branch__name', 'name')


class Post(Record):
    title = models.CharField(max_length=128)
    content = SummernoteTextField(null=True)
    is_draft = models.BooleanField(default=True)

    category = models.ForeignKey(
        PostCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    tags = models.ManyToManyField(
        PostTag,
        blank=True
    )

    def __str__(self):
        return self.title


class PostIdea(Record):
    title = models.CharField(max_length=128)
    is_realized = models.BooleanField(default=False)

    category = models.ForeignKey(
        PostCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    tags = models.ManyToManyField(
        PostTag,
        blank=True
    )

    def __str__(self):
        return self.title
