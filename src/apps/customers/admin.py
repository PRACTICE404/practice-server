from django.contrib import admin

from . import models


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
