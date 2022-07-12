# Импортирую get_object_or_404, которая позволит найти объект под нужным номером или отобразит 404
from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    # order_by('-date')[:5] - будет отображать самые свежие публикации и отображать последние 5 постов
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

# Принимает переменную "blog_id" из urls.py
def detail(request, blog_id):
    # pk - термин по работе с базами данных, который означает первичный ключ
    # pk пытается найти конкретный объект под нужным номером, и если у нее не получается, то возвращает 404
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})