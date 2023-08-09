from django.urls import path
from writer.writer_views import posts_views

urlpatterns = [
    path("", posts_views.EditorListView.as_view(), name="posts_list"),
    path("create/", posts_views.EditorCreatePostView.as_view(), name="post_create"),
    path("<pk>/<slug>/edit/", posts_views.EditPostView.as_view(), name="post_edit"),
]