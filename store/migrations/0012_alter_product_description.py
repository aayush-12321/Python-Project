# Generated by Django 5.0.3 on 2024-03-26 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]
