# Generated by Django 2.0.2 on 2018-04-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0028_literature_god'),
    ]

    operations = [
        migrations.AlterField(
            model_name='literature',
            name='god',
            field=models.DateField(default=''),
        ),
    ]
