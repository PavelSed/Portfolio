from django.shortcuts import render
from .models import Blog

def all_blogs(request):
    # order_by('-date')[:5] - будет отображать самые свежие публикации и отображать последние 5 постов
    projects = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'projects':projects})