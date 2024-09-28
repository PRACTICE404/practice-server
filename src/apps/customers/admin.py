from django.contrib import admin

from apps.positions.project_manager.admin import admin_site as project_manager_admin_site  # NOQA
from . import models


@admin.register(models.Customer, site=project_manager_admin_site)
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'nickname',
        'created',
        'updated'
    )
    search_fields = (
        'nickname',
        'id'
    )
