from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField('Created Date', default=timezone.now)
    title = models.CharField('Title', max_length=200)
    content = models.TextField('Content')
    slug = models.SlugField('Slug')
    view_count = models.IntegerField("View Count", default=0)

    def get_absolute_url(self):
        return reverse("post", args=[self.slug])

    def __str__(self):
        return f'"{self.title}" bypython manage.py migrate {self.author}'