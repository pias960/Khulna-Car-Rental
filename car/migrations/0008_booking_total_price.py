# Generated by Django 5.0.3 on 2024-03-15 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_booking_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total_price',
            field=models.IntegerField(default=25),
            preserve_default=False,
        ),
    ]