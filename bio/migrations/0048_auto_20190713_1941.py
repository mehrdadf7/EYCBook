# Generated by Django 2.2.3 on 2019-07-13 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0047_auto_20190713_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipmentuseful',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='favoriteequipment',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]