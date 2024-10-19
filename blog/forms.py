from django import forms
from django.forms.renderers import DjangoTemplates
from django.utils import timezone

from blog.models import Post


class Renderer(DjangoTemplates):
    form_template_name = "blog/forms/div.html"


class TiptapWidget(forms.Textarea):
    template_name = "blog/forms/widgets/tiptap.html"

    class Media:
        js = ("dist/tiptap.js",)


class PostForm(forms.ModelForm):
    default_renderer = Renderer

    required_css_class = 'required'
    error_css_class = 'has-error'

    title = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input input-bordered"})
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "input input-bordered", "type": "date"}),
        initial=timezone.now,
    )
    body = forms.CharField(widget=TiptapWidget())

    class Meta:
        model = Post
        fields = ["title", "date", "body"]
