# Generated by Django 5.0.3 on 2024-03-12 18:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_alter_car_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rental',
            new_name='Booking',
        ),
    ]
