# Generated by Django 5.0.3 on 2024-03-16 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0013_remove_booking_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='cost_par_day',
            field=models.IntegerField(),
        ),
    ]