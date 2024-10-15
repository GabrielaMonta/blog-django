from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify
import uuid


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    content = models.TextField(max_length=10000)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now)
    modification_date = models.DateTimeField(auto_now=True)
    allow_comments = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    @property
    def amount_comments(self):
        return self.comments.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
            super().save(*args, **kwargs)
        # TODO: Definir imagenes portada

    def generate_unique_slug(self):
        # tenemos este titulo para el post
        # tenemos-este-titulo-para-el-postCLASE23.md 2024-09-24
        3 / 6
        # tenemos-este-titulo-para-el-post-1
        # tenemos-este-titulo-para-el-post-2
        # tenemos-este-titulo-para-el-post-3
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug
