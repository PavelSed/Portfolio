from django.urls import path
# !Импортируем views из портфолио
from . import views

# Задает имя приложения 'blog', чтобы проще ориентироваться при росте проекта. Помогает исключить возможные ошибки
app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    # Считывает числовое значение и записывает его в переменную "blog_id"
    path('<int:blog_id>/', views.detail, name='detail')
]