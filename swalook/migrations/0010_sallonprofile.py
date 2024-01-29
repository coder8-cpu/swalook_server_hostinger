# Generated by Django 4.0.6 on 2023-03-12 14:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('swalook', '0009_delete_vendor_inv_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='SallonProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('salon_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('owner_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('owner_address', models.CharField(blank=True, max_length=1000, null=True)),
                ('owner_contactno', models.CharField(blank=True, max_length=1000, null=True)),
                ('owner_Panno', models.CharField(blank=True, max_length=1000, null=True)),
                ('owner_cgst_no', models.CharField(blank=True, max_length=1000, null=True)),
                ('owner_email', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
