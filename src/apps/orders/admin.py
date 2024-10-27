from django.db.models import Sum
from django.contrib import admin
from django.utils.html import format_html

from apps.payments.models import Account
from . import models


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'id',
        'hours_spent',
        'estimate',
        'epic',
        'is_backlog',
        'status',
    )
    list_editable = (
        'status',
        'is_backlog'
    )
    list_filter = (
        'is_backlog',
        'status'
    )
    search_fields = (
        'id',
        'title',
        'epic__title',
        'epic__order__title'
    )
    autocomplete_fields = (
        'epic',
    )

    def hours_spent(self, obj):
        minutes = obj.session_distributions.aggregate(Sum('minutes'))['minutes__sum']  # NOQA

        if minutes == 0 or minutes is None:
            return 0
        else:
            return f'{round(minutes / 60, 2)} ({round(minutes / 60 / obj.estimate * 100, 1)}%)'  # NOQA


class TaskInline(admin.TabularInline):
    model = models.Task
    fields = (
        'title',
        'estimate',
        'status',
        'is_backlog',
    )


@admin.register(models.OrderHistory)
class OrderHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'text',
        'updated',
        'created'
    )
    autocomplete_fields = (
        'order',
    )


@admin.register(models.Epic)
class EpicAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'id',
        'hours_spent',
        'estimate',
        'order'
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

    def hours_spent(self, obj):
        minutes = obj.tasks.aggregate(Sum('session_distributions__minutes'))['session_distributions__minutes__sum']  # NOQA

        if minutes == 0 or minutes is None:
            return 0
        else:
            return f'{round(minutes / 60, 2)} ({round(minutes / 60 / obj.estimate * 100, 1)}%)'  # NOQA


class EpicInline(admin.TabularInline):
    model = models.Epic
    show_change_link = True
    extra = 0
    classes = ['collapse']


class HistoryInline(admin.TabularInline):
    model = models.OrderHistory
    show_change_link = True
    extra = 0
    classes = ['collapse']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'id',
        'hours_spent',
        'estimate',
        'deposits_made',
        'status',
        'project'
    )
    list_editable = (
        'status',
    )
    list_filter = (
        'status',
    )
    inlines = (
        EpicInline,
        HistoryInline
    )
    search_fields = (
        'id',
        'title'
    )
    autocomplete_fields = (
        'project',
    )

    def hours_spent(self, obj):
        minutes = obj.epics.aggregate(Sum('tasks__session_distributions__minutes'))['tasks__session_distributions__minutes__sum']  # NOQA

        if minutes == 0 or minutes is None:
            return 0
        else:
            return f'{round(minutes / 60, 2)} ({round(minutes / 60 / obj.estimate * 100, 1)}%)'  # NOQA

    def deposits_made(self, obj):
        # value = obj.deposit_distributions.aggregate(Sum('value'))['value__sum']  # NOQA
        values = [
            f"{obj.deposit_distributions.filter(deposit__account=account).aggregate(Sum('value'))['value__sum']} {account.currency}" for  # NOQA
            account in Account.objects.all()
        ]
        return format_html(',<br>'.join(values))
