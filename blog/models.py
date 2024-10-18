from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils import timezone

from utils import nanoid


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(live=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=205, unique=True, editable=False)
    body = models.TextField()
    date = models.DateField()
    live = models.BooleanField(default=False, editable=False)
    objects = PostQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.title)}-{nanoid.generate(size=5)}"
        return super().save(*args, **kwargs)

    def publish(self, commit=True, *args, **kwargs):
        self.date = timezone.now()
        self.live = True

        if commit:
            self.save(*args, **kwargs)


class Image(models.Model):
    post = models.ForeignKey(Post, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog-images/")
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.caption
