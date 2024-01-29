# Generated by Django 4.0.6 on 2023-01-15 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swalook', '0002_invoice_check_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='c_gst',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='s_gst',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
    ]
