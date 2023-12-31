# Generated by Django 4.0.5 on 2023-04-16 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0002_alter_sales_item_mrp_alter_sales_item_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='Item_Fat_Content',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Item_MRP',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Item_Visibility',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Item_Weight',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Outlet_Size',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Outlet_Type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='item_type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
