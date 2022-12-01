# Generated by Django 3.2.16 on 2022-11-30 16:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20221130_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='коллво голосов'),
        ),
        migrations.AlterField(
            model_name='question',
            name='life_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 23, 47, 28, 159637), verbose_name='Время жизни'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 30, 23, 47, 28, 159637), verbose_name='Дата'),
        ),
    ]