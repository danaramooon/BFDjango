# Generated by Django 2.1.1 on 2018-10-05 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20181006_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_on',
            field=models.CharField(max_length=100),
        ),
    ]