# Generated by Django 5.2.2 on 2025-07-07 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_warrantyitem_product_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='warrantyitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
