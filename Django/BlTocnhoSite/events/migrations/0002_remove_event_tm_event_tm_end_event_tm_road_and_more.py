# Generated by Django 4.1.2 on 2022-10-27 10:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='tm',
        ),
        migrations.AddField(
            model_name='event',
            name='tm_end',
            field=models.TimeField(blank=True, default=datetime.time(0, 0), verbose_name='Время Ивента (конец)'),
        ),
        migrations.AddField(
            model_name='event',
            name='tm_road',
            field=models.TimeField(blank=True, default=datetime.time(0, 0), verbose_name='Время на дорогу'),
        ),
        migrations.AddField(
            model_name='event',
            name='tm_start',
            field=models.TimeField(blank=True, default=datetime.time(0, 0), verbose_name='Время Ивента (начало)'),
        ),
    ]
