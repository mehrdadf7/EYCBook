# Generated by Django 2.2.3 on 2019-07-18 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0059_auto_20190718_1920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipment',
            old_name='equipment_info',
            new_name='equipments_info',
        ),
        migrations.RenameField(
            model_name='equipmentuseful',
            old_name='equipment_info',
            new_name='equipments_info',
        ),
    ]