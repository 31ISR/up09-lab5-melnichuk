from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Communities(models.Model):
    name = models.CharField('Название', max_length=75)
    description = models.TextField('Описание', max_length=150)
    slug = models.SlugField('Краткий заголовок')
    date = models.DateTimeField('Дата', auto_now_add=True)
    free = models.BooleanField('Свододно для вступления', )
    banner = models.ImageField('Изображение', default='fallback.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)


    def __str__(self):
        return self.name