from django.contrib import admin
from django.db.models import Sum

from apps.base.admin import list_display_of_record
from . import models


@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'code',
        *list_display_of_record
    )


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'currency',
        *list_display_of_record
    )


class DepositDistributionInline(admin.TabularInline):
    model = models.DepositDistribution


@admin.register(models.Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = (
        'account',
        'value',
        'is_distributed',
        *list_display_of_record
    )

    def get_inlines(self, request, obj):
        if not obj:
            return ()

        return (
            DepositDistributionInline,
        )

    def is_distributed(self, obj):
        return '✅' if obj.distributions.aggregate(Sum('value'))['value__sum'] == obj.value else '❌'  # NOQA


@admin.register(models.Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    list_display = (
        'account',
        'value',
        *list_display_of_record
    )


@admin.register(models.Swap)
class SwapAdmin(admin.ModelAdmin):
    list_display = (
        'account_from',
        'value_from',
        'account_to',
        'value_to',
        *list_display_of_record
    )
