# Generated by Django 2.0.2 on 2018-04-19 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_auto_20180419_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zert_jumys',
            name='opisanie',
            field=models.CharField(default='Some', max_length=100),
        ),
    ]
