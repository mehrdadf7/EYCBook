# Generated by Django 2.2.3 on 2019-07-11 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0003_auto_20190711_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoriteequipment',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]