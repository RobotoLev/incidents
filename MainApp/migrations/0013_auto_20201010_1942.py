# Generated by Django 3.1.2 on 2020-10-10 16:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0012_auto_20201010_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='communications_object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MainApp.communications', verbose_name='Объект коммуникаций, для которого вводится инцидент'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 10, 19, 42, 25, 490430), verbose_name='Дата и время начала'),
        ),
    ]
