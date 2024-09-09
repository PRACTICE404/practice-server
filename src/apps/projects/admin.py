from django.contrib import admin

from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'customer',
        'updated',
        'created'
    )
    autocomplete_fields = (
        'customer',
    )
