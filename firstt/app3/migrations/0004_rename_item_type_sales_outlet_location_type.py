# Generated by Django 4.0.5 on 2023-04-18 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0003_alter_sales_item_fat_content_alter_sales_item_mrp_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales',
            old_name='item_type',
            new_name='Outlet_location_type',
        ),
    ]
