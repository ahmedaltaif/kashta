from django.contrib import admin
from django.utils.html import format_html
from .models import Article, Topic

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 45px; height: 45px;" />'.format(obj.image.url))
        return ""

    image_preview.short_description = 'Image Preview'

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
