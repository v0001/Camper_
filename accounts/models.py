from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField('닉네임', max_length=20, null = True)

    location = models.CharField('장소', max_length=50, null = True)
    age = models.PositiveIntegerField('나이', default=1, null = True)
    
    def __str__(self):
        return str