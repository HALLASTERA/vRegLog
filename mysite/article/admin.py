from django.contrib import admin
from article.models import Article

from django.core import serializers
from django.http import HttpResponse


# Register your models here.


def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title1', 'status']
    ordering = ['title1']
    actions = [export_as_json]






admin.site.register(Article, ArticleAdmin)