from django.contrib import admin

from . import models


@admin.register(models.WorkingExperience)
class WorkingExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'company_name',
        'position_name',
        'year_start',
        'year_end',
    )
