# Generated by Django 3.1.2 on 2020-10-10 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_communications_communicationstype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='communications',
            options={'verbose_name': 'объект коммуникаций', 'verbose_name_plural': 'объекты коммуникаций'},
        ),
        migrations.AlterModelOptions(
            name='communicationstype',
            options={'verbose_name': 'тип объекта коммуникаций', 'verbose_name_plural': 'типы объектов коммуникаций'},
        ),
        migrations.AddField(
            model_name='communications',
            name='parameters',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='communicationstype',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Тип объекта коммуникаций'),
        ),
    ]