# Generated by Django 2.1.1 on 2018-11-03 13:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20181103_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 3, 19, 17, 25, 558095)),
        ),
    ]
