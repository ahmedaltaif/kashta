from django.contrib import admin
from .models import Article, Topic
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.utils.html import format_html

class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ['title', 'topic', 'published_date', 'view_count']
    search_fields = ['title', 'content']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Topic)
