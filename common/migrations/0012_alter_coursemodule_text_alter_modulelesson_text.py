# Generated by Django 4.2 on 2024-09-28 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_remove_coursemodule_lesson_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodule',
            name='text',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='modulelesson',
            name='text',
            field=models.CharField(max_length=250),
        ),
    ]
