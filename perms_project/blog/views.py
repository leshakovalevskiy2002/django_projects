from guardian.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin as DjangoPermissionRequiredMixin
from django.views.generic import CreateView, UpdateView

from blog.models import Post


class CreatePostView(DjangoPermissionRequiredMixin, CreateView):
    permission_required = ['blog.add_post']
    model = Post
    fields = ('name', 'content')
    template_name = 'post.html'


class PostDetailView(PermissionRequiredMixin, UpdateView):
    model = Post
    fields = "__all__"
    permission_required = 'blog.change_post'
    raise_exception = True
    template_name = "post_detail.html"
