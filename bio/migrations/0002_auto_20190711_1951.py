# Generated by Django 2.2.3 on 2019-07-11 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmentcategory',
            name='equipment',
        ),
        migrations.AddField(
            model_name='equipment',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bio.EquipmentCategory'),
        ),
    ]