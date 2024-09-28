from django.contrib import admin

from apps.positions.project_manager.admin import admin_site as project_manager_admin_site  # NOQA
from apps.base.admin import list_display_of_record

from . import models


@admin.register(models.Session, site=project_manager_admin_site)
@admin.register(models.Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        'minutes_working',
        'id',
        *list_display_of_record
    )
