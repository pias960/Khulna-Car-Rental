# Generated by Django 5.0.3 on 2024-03-12 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_rename_rental_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='car',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='car.car'),
        ),
    ]
