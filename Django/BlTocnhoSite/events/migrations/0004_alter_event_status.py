# Generated by Django 4.1.1 on 2022-09-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Запланированно'), ('SUCCES', 'Успешно выполненное'), ('NO_SUCCES', 'Не выполненное'), ('PENDING', 'Отложенное'), ('CANCEL', 'Отмененно'), ('In processing', 'Выполняется'), ('passed', 'Прошло')], default=('ACTIVE', 'Запланированно'), max_length=255),
        ),
    ]
