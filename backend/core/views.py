from rest_framework.viewsets import ModelViewSet
from .models.post import Post
from .serializers import PostSerializer

class PostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

