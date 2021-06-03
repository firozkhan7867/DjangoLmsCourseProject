# Generated by Django 3.1.1 on 2021-05-05 08:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0002_remove_blog_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]