# Generated by Django 2.0.2 on 2018-04-19 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0023_auto_20180419_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='literature',
            name='godd',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]