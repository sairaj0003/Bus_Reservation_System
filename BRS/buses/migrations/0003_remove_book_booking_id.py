# Generated by Django 5.0.3 on 2024-03-30 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0002_book_alter_bus_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='booking_id',
        ),
    ]
