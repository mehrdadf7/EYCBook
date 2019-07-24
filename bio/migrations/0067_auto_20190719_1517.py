# Generated by Django 2.2.3 on 2019-07-19 15:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0066_auto_20190719_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentuseful',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipmentuseful',
            name='publish',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='equipmentuseful',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]