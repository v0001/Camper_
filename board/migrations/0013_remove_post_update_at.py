# Generated by Django 3.1 on 2020-08-25 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0012_auto_20200823_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='update_at',
        ),
    ]