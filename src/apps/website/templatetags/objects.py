from django import template

from apps.marketplaces.models import MarketplaceAccount
from apps.services.models import Service, TechnologyArea, Faq
from apps.socials.models import SocialNetworkAccount
from apps.website.models import Stats, WebsiteSettings


register = template.Library()


@register.simple_tag
def get_marketplace_accounts():
    return MarketplaceAccount.objects.all()


@register.simple_tag
def get_services():
    return Service.objects.all()


@register.simple_tag
def get_technology_areas():
    return TechnologyArea.objects.all()


@register.simple_tag
def get_faq():
    return Faq.objects.all()


@register.simple_tag
def get_social_accounts():
    return SocialNetworkAccount.objects.all()


@register.simple_tag
def get_stats():
    return Stats.load()


@register.simple_tag
def get_website_settings():
    return WebsiteSettings.load()
