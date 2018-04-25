# Generated by Django 2.0.2 on 2018-04-17 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20180417_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='literature',
            name='author',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='literature',
            name='god',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='literature',
            name='izdanie',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='literature',
            name='stranica',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='zert_jumys',
            name='opisanie',
            field=models.CharField(default='', max_length=100),
        ),
    ]
