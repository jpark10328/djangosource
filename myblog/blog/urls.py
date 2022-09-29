from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/blog/post/
    path("post/", views.posts_list, name="posts_list"),
    path("write/", views.posts_write, name="posts_write"),
]
