# Generated by Django 3.1.6 on 2021-02-15 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mileage', '0002_auto_20210214_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
