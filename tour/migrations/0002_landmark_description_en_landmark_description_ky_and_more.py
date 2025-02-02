# Generated by Django 5.0.6 on 2024-06-28 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='landmark',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='landmark',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='landmark',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.RemoveField(
            model_name='guide',
            name='excursions',
        ),
        migrations.RemoveField(
            model_name='guide',
            name='tours',
        ),
        migrations.AddField(
            model_name='guide',
            name='excursions',
            field=models.ManyToManyField(to='tour.landmark'),
        ),
        migrations.AddField(
            model_name='guide',
            name='tours',
            field=models.ManyToManyField(to='tour.tour'),
        ),
    ]
