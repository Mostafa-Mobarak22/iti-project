# Generated by Django 5.1.1 on 2024-09-26 00:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_propertyimage'),
        ('user', '0007_remove_user_address_remove_user_another_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='another_phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, choices=[('EG', 'Egypt')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user/images/profile/'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_company',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='property_ids',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='property.property'),
        ),
        migrations.AddField(
            model_name='user',
            name='register_photo',
            field=models.ImageField(blank=True, null=True, upload_to='user/images/register/'),
        ),
        migrations.AddField(
            model_name='user',
            name='street',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(default=1, max_length=25, unique=True),
            preserve_default=False,
        ),
    ]
