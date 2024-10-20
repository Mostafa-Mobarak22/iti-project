# Generated by Django 5.1.1 on 2024-10-15 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_alter_property_listed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='commercial',
            field=models.CharField(choices=[('Office', 'Office'), ('Retail', 'Retail'), ('Restaurant', 'Restaurant'), ('Pharmacy', 'Pharmacy'), ('Clinic', 'Clinic'), ('Commercial Building', 'Commercial Building'), ('Commercial Land', 'Commercial Land'), ('Agricultural', 'Agricultural'), ('Warehouse', 'Warehouse'), ('Garage', 'Garage'), ('Showroom', 'Showroom'), ('Co-Working Space', 'Co-Working Space'), ('Medical Facility', 'Medical Facility'), ('Other Commercial', 'Other Commercial'), ('Apartment', 'Apartment'), ('Villa', 'Villa'), ('Duplex', 'Duplex'), ('Penthouse', 'Penthouse'), ('Chalet', 'Chalet'), ('Townhouse', 'Townhouse'), ('Twin House', 'Twin House'), ('Room', 'Room'), ('Cabin', 'Cabin'), ('Roof', 'Roof'), ('iVilla', 'iVilla'), ('Hotel Apartment', 'Hotel Apartment'), ('Residential Land', 'Residential Land'), ('Other Residential', 'Other Residential')], max_length=20),
        ),
    ]
