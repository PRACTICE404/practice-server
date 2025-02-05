from django.contrib import admin

from . import models


@admin.register(models.Stats)
class StatsAdmin(admin.ModelAdmin):
    list_display = (
        'years',
        'projects',
        'customers'
    )


@admin.register(models.WebsiteSettings)
class WebsiteSettings(admin.ModelAdmin):
    list_display = (
        'consultation_price',
        'slogan',
        'location'
    )
