# Generated by Django 2.2.3 on 2019-07-13 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0043_auto_20190713_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='MagazineInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField(blank=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='equipment',
            options={},
        ),
        migrations.AlterModelOptions(
            name='equipmentuseful',
            options={},
        ),
        migrations.AlterModelOptions(
            name='magazine',
            options={'ordering': ['id']},
        ),
    ]