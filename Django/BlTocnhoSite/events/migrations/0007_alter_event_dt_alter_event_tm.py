# Generated by Django 4.1.2 on 2022-10-19 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_event_dt_alter_event_tm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='dt',
            field=models.DateField(blank=True, default=None, verbose_name='Дата Ивента'),
        ),
        migrations.AlterField(
            model_name='event',
            name='tm',
            field=models.TimeField(blank=True, default=None, verbose_name='Время Ивента'),
        ),
    ]