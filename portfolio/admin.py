from django.contrib import admin
from .models import Project # Импортируем созданную модель

# Регистрирует модель
admin.site.register(Project)


