from django.contrib import admin

from apps.positions.project_manager.admin import admin_site as project_manager_admin_site  # NOQA
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


@admin.register(models.DepositDistribution, site=project_manager_admin_site)
@admin.register(models.DepositDistribution)
class DepositDistributionAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'deposit',
        'value'
    )


class DepositDistributionInline(admin.TabularInline):
    model = models.DepositDistribution


@admin.register(models.Deposit, site=project_manager_admin_site)
@admin.register(models.Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = (
        'account',
        'value',
        *list_display_of_record
    )
    inlines = (
        DepositDistributionInline,
    )


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
