from django.contrib import admin
from .models import Article, Topic

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'view_count', 'summary')
    search_fields = ('title', 'content')

class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Topic, TopicAdmin)
