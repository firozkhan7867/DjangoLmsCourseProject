# Generated by Django 3.1.1 on 2021-05-05 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='student',
        ),
    ]
