# Generated by Django 5.1.1 on 2024-09-25 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_another_phone_user_property_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(choices=[('EG', 'Egypt')], max_length=2),
        ),
    ]
