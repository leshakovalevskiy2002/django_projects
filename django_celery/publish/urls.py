from django.urls import path
from .views import view_post

urlpatterns = [
    path('<slug:slug>/', view_post, name="post"),
]