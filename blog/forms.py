from django import forms
from django.forms.renderers import DjangoTemplates
from django.utils import timezone

from blog.models import Post


class Renderer(DjangoTemplates):
    form_template_name = "blog/forms/div.html"

class Textarea(forms.Textarea):
    template_name = "blog/forms/textarea.html"

class PostForm(forms.ModelForm):
    default_renderer = Renderer

    title = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input input-bordered"})
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "input input-bordered", "type": "date"}),
        initial=timezone.now,
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "textarea textarea-bordered min-h-[250px] [field-sizing:content]"
            }
        )
    )

    class Meta:
        model = Post
        fields = ["title", "date", "body"]
