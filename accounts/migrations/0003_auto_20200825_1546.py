# Generated by Django 3.1 on 2020-08-25 06:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20200819_1608'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='mypage',
        ),
    ]