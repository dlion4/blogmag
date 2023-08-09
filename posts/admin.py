from django.contrib import admin
from posts.forms.admin import PostAdminForm
# Register your models here.
from posts.models import (
    Post,
PostComment,
PostImage,
CommentReply
)

class PostImageInline(admin.StackedInline):
    model = PostImage
    extra=0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display=['writer',"topic","title","createdAt","updatedAt",
                 "views","comments"]
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ['writer', "topic", "tags"]
    search_field = ['topic', 'title', 'tags']
    list_per_page = 20
    inlines = (PostImageInline, )
    
@admin.register(PostComment)
class PostComment(admin.ModelAdmin):
    list_display =[
        "post", "email", "full_name", "postedAt"
    ]


@admin.register(CommentReply)
class AdminReply(admin.ModelAdmin):
    pass