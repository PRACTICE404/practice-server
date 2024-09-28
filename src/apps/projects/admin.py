from django.contrib import admin

from apps.positions.project_manager.admin import admin_site as project_manager_admin_site  # NOQA
from . import models


@admin.register(models.Project, site=project_manager_admin_site)
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
        'title',
    )
