# Generated by Django 5.1.1 on 2024-09-26 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_property_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='another_phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_company',
        ),
        migrations.RemoveField(
            model_name='user',
            name='property_ids',
        ),
        migrations.RemoveField(
            model_name='user',
            name='register_photo',
        ),
        migrations.RemoveField(
            model_name='user',
            name='street',
        ),
    ]
