# Generated by Django 2.2.3 on 2019-07-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0027_remove_creator_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
