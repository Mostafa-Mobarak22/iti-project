# Generated by Django 5.1.1 on 2024-10-15 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_user_member_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='wish',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
