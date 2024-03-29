# Generated by Django 3.1.3 on 2020-12-22 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnapp', '0011_auto_20201221_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('date_enter', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
