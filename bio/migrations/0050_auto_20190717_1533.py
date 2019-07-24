# Generated by Django 2.2.3 on 2019-07-17 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0049_auto_20190714_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmentcategory',
            name='equipments',
        ),
        migrations.AddField(
            model_name='equipmentcategory',
            name='equipments',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bio.Equipment'),
            preserve_default=False,
        ),
    ]