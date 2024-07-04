from django.db import models
from ckeditor.fields import RichTextField

class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=200)
    content = RichTextField()  # Changed to RichTextField
    image = models.ImageField(upload_to='articles/images/', blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
