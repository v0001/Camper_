from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    nickname = models.CharField('닉네임', max_length=20, blank=True, null=True)
    #blacktrue->빈칸입력가능 nulltrue -> 데이터의공백 빈칸입력불가

    location = models.CharField('장소', max_length=50, blank=True, null=True)
    age = models.PositiveIntegerField('나이', default=1, blank=True, null=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)