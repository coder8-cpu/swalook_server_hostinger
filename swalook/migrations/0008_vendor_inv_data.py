# Generated by Django 4.0.6 on 2023-03-12 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('swalook', '0007_alter_invoice_grand_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='vendor_inv_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Address', models.CharField(blank=True, max_length=200, null=True)),
                ('Mobileno', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('service_catg_name', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField(null=True)),
                ('prise', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('service_by', models.CharField(max_length=40)),
                ('slno', models.CharField(blank=True, max_length=50, null=True)),
                ('s_gst', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('c_gst', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('gst_number', models.CharField(blank=True, max_length=20, null=True)),
                ('Discont', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('total_prise', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100, null=True)),
                ('total_tax', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100, null=True)),
                ('total_discount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100, null=True)),
                ('total_quantity', models.IntegerField(default=0)),
                ('total_cgst', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100, null=True)),
                ('total_sgst', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100, null=True)),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100, null=True)),
                ('s_gst_percent', models.CharField(max_length=30)),
                ('c_gst_percent', models.CharField(max_length=30)),
                ('vendorname', models.CharField(max_length=30)),
                ('check_value', models.CharField(blank=True, max_length=30, null=True)),
                ('date_field', models.DateField()),
                ('vendor_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]