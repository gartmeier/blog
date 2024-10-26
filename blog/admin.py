from django.contrib import admin
from django.contrib.admin import register
from django.forms import widgets
from django.db import models

from blog.models import Post, Image


@register(Post)
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            "widget": widgets.Textarea(
                attrs={
                    "style": "width: 120ch; height: 50ch; font-size: 20px; line-height: 1.5"
                }
            )
        },
    }


@register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
