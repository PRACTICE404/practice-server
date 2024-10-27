from django.contrib import admin

from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'id',
        'customer',
        'updated',
        'created'
    )
    autocomplete_fields = (
        'customer',
    )
    search_fields = (
        'id',
        'title'
    )
