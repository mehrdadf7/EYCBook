# Generated by Django 2.2.3 on 2019-07-12 05:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0004_auto_20190711_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='favoriteequipment',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]