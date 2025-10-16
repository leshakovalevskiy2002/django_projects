from django.urls import path
from .views import home_view, group_chat_view


urlpatterns = [
    path('', home_view, name="home"),
    path('groups/<uuid:uuid>/', group_chat_view, name="group"),
]