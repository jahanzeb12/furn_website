# Generated by Django 3.1.3 on 2020-12-21 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furnapp', '0007_order_transaction_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category_name',
            new_name='category',
        ),
    ]