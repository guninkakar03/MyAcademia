# Generated by Django 4.2.2 on 2023-06-29 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_programarea'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='programArea',
            new_name='program_area',
        ),
    ]
