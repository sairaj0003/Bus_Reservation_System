# Generated by Django 5.0.3 on 2024-03-08 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='re_enter_password',
        ),
    ]
