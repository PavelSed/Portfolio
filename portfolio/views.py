from django.shortcuts import render
# Импортируем проект из модели
from .models import Project


def home(request):
    # Импортирует все объекты из базы данных (все записи о проекте из базы данных)
    projects = Project.objects.all()
    # Импортируем все записи из базы данных с помощью словаря
    return render(request, 'portfolio/home.html', {'projects':projects})