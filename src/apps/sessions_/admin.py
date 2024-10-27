from django.db.models import Sum
from django.contrib import admin

from apps.base.admin import list_display_of_record

from . import models


class SessionDistributionInline(admin.TabularInline):
    model = models.SessionDistribution


@admin.register(models.Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        'minutes_working',
        'id',
        'is_distributed',
        *list_display_of_record
    )
    inlines = (
        SessionDistributionInline,
    )

    def is_distributed(self, obj):
        return '✅' if obj.distributions.aggregate(Sum('minutes'))['minutes__sum'] == obj.minutes_working else '❌'  # NOQA
