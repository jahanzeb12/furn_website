# Generated by Django 3.1.3 on 2020-12-10 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnapp', '0004_auto_20201204_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
