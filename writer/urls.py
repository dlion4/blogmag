from django.urls import path, include
from . import views

app_name = "writer"

urlpatterns = [
    path("posts/", include("writer.writer_urls.posts_urls")),
]
