from django.contrib import admin

from . import models


@admin.register(models.SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


@admin.register(models.SocialNetworkAccount)
class SocialNetworkAccountAdmin(admin.ModelAdmin):
    list_display = (
        'link',
        'social_network'
    )
