# Generated by Django 2.2.3 on 2019-07-12 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0018_remove_equipment_date_of_create_equipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='image',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='favoriteequipment',
            name='image',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]