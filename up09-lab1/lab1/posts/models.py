from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField('Название', max_length=75)
    body = models.TextField('Описание')
    slug = models.SlugField('Краткое наименование')
    date = models.DateTimeField('Дата', auto_now_add=True)
    banner = models.ImageField('Изображение', default='fallback.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)


    def __str__(self):
        return self.title