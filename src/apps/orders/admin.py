from django.contrib import admin

from . import models


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'id',
        'epic',
        'is_backlog',
        'status',
        'estimate',
        'created',
        'updated'
    )
    list_filter = (
        'is_backlog',
        'status'
    )
    search_fields = (
        'id',
        'title'
    )
    autocomplete_fields = (
        'epic',
    )


class TaskInline(admin.TabularInline):
    model = models.Task
    fields = (
        'title',
        'estimate',
        'status',
        'is_backlog',
    )


@admin.register(models.Epic)
class EpicAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'id',
        'order',
        'estimate',
        'updated',
        'created'
    )
    search_fields = (
        'id',
        'title'
    )
    autocomplete_fields = (
        'order',
    )
    inlines = (
        TaskInline,
    )


class EpicInline(admin.TabularInline):
    model = models.Epic


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'id',
        'project',
        'estimate',
        'updated',
        'created'
    )
    inlines = (
        EpicInline,
    )
    search_fields = (
        'id',
        'title'
    )
    autocomplete_fields = (
        'project',
    )
