from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хипы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('gildmaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    )
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    category = models.CharField(max_length=16, choices=TYPE, default='tank')
    upload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.title


class UserResponse(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    status= models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)