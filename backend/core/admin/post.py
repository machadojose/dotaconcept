from ..models.post import Post
from django.contrib.admin import ModelAdmin, register


@register(Post)
class PostAdmin(ModelAdmin):
    list_display = ["title"]
