from django.db import models
from guardian.models import UserObjectPermission


class Post(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.name