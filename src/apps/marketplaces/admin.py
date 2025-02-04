from django.contrib import admin

from . import models


@admin.register(models.Marketplace)
class MarketplaceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(models.MarketplaceAccount)
class MarketplaceAccountAdmin(admin.ModelAdmin):
    list_display = (
        'marketplace',
        'name',
        'is_active'
    )
    list_editable = (
        'is_active',
    )
    list_filter = (
        'is_active',
    )


@admin.register(models.Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = (
        'date_sent',
        'customer_title',
        'customer_feedback',
        'status',
        'marketplace_account',
        'customer'
    )
    list_editable = (
        'status',
    )
    list_filter = (
        'status',
        'customer_feedback'
    )
