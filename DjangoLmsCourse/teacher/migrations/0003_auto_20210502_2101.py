# Generated by Django 3.1.1 on 2021-05-02 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20210502_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='communication_skills_percentage',
            new_name='communication_skills',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='programming_skills_percentage',
            new_name='programming_skills',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='teching_skills_percentage',
            new_name='teching_skills',
        ),
    ]
