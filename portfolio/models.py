from django.db import models

# Создает класс, которые представляет модель и обеспечивает взаимодействие с базой данных в джанго
# Модель необходима для создания таблицы и добавления в нее данных

class Project(models.Model):
    # Означает, что в заголовке title будет не более 100 символов
    # CharField - cтроковое поле, для строк малого и большого размера
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)