from rest_framework.serializers import ModelSerializer
from .models.post import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body']