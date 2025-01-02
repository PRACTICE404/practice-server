from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils.html import format_html

from . import models
from . import consts


@admin.register(models.ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(models.Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'programming_language',
        'area'
    )
    list_filter = (
        'programming_language',
        'area',
    )
    search_fields = (
        'name',
        'programming_language__name'
    )


@admin.register(models.TechnologyArea)
class TechnologyAreaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )


class FaqInline(admin.StackedInline):
    model = models.Faq


class PassShowTechnologyAreas(SimpleListFilter):
    title = ''
    parameter_name = consts.SERVICE_SHOW_TECHNOLOGY_AREAS_GET_PARAM_NAME

    def lookups(self, request, model_admin):
        return (request.GET.get(self.parameter_name), ''),

    def queryset(self, request, queryset):
        return queryset


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    change_list_template = "admin/services/service/change_list.html"
    list_filter = (
        'technology_areas',
        'is_active',
        PassShowTechnologyAreas
    )
    inlines = (
        FaqInline,
    )
    autocomplete_fields = (
        'technology_areas',
    )

    def related_technology_areas(self, obj):
        if _ := obj.technology_areas.all():
            return format_html("<br/>".join([obj.name for obj in _]))
        else:
            return "-"

    def get_list_display(self, request):
        return (
            'title',
            *(('related_technology_areas', )
                if request.GET.get(consts.SERVICE_SHOW_TECHNOLOGY_AREAS_GET_PARAM_NAME) == '1'  # NOQA
                else ()),
            'is_active'
        )

    def get_list_editable(self, request):
        return (
            'is_active',
        )


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'service',
        'is_fake',
        'is_finished'
    )
    list_filter = (
        'is_fake',
        'is_finished'
    )
    autocomplete_fields = (
        'project',
    )


@admin.register(models.Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = (
        'text_question',
        'service'
    )
