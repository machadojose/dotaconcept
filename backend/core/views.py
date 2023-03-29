# from django.shortcuts import render
from django.http import JsonResponse

from .models.post import Post

# Create your views here.


def index(request):
    posts = list(Post.objects.all().values())
    return JsonResponse(posts, safe=False)
