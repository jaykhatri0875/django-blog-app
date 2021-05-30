from django.shortcuts import get_list_or_404, render, get_object_or_404
from .models import Post

def post_list(request):
    #posts = Post.published.all()
    posts = get_list_or_404(Post)
    return render(request,
                'post/list.html',
                {'posts': posts})

def post_detail(request, post):
    post = get_object_or_404(Post, slug=post)
    return render(request,
                  'post/detail.html',
                  {'post': post})
