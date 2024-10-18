from django.contrib import admin
from django.contrib.admin import register

from blog.models import Post, Image


@register(Post)
class ArticleAdmin(admin.ModelAdmin):
    pass


@register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
