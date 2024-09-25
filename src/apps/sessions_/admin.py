from django.contrib import admin

from apps.base.admin import list_display_of_record

from . import models


@admin.register(models.Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        'minutes_working',
        'id',
        *list_display_of_record
    )
