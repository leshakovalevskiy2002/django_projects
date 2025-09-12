from django.contrib import admin
from blog.models import Post
from guardian.admin import GuardedModelAdmin


class PostAdmin(GuardedModelAdmin):
    list_display = ('name',)


admin.site.register(Post, PostAdmin)