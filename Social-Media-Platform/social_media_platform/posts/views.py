from django.shortcuts import render

# Create your views here.

# posts/views.py

from django.shortcuts import render
from .models import Post

def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/feed.html', {'posts': posts})
