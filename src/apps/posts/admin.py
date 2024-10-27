from django_summernote.admin import SummernoteModelAdmin

from django.contrib import admin

from . import models


@admin.register(models.PostBranch)
class PostBranchAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(models.PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'branch'
    )


@admin.register(models.PostTag)
class PostTagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(models.Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = (
        'title',
        'content',
        'category',
    )


@admin.register(models.PostIdea)
class PostIdeaAdmin(admin.ModelAdmin):
    summernote_fields = ('content',)
    list_display = (
        'title',
        'category',
        'is_realized'
    )
