# Generated by Django 4.2.2 on 2023-07-07 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_rename_distrubution_course_distribution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='avg_rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
    ]
