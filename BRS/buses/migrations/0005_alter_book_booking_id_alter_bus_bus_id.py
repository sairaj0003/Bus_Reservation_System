# Generated by Django 5.0.3 on 2024-03-30 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0004_book_booking_id_bus_bus_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='booking_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bus',
            name='bus_id',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]