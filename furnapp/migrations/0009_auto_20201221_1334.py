# Generated by Django 3.1.3 on 2020-12-21 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnapp', '0008_auto_20201221_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='street_no',
        ),
        migrations.AddField(
            model_name='shipping',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
