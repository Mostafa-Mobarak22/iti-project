from django.db import models
from ads.models import *
# Create your models here.
class Property(models.Model):
    property_type = [
        ('residential', 'Residential'),
        ('commercial', 'Commercial'),
    ]
    commercial_type = [
    ('office', 'Office'),
    ('retail', 'Retail'),
    ('restaurant', 'Restaurant'),
    ('pharmacy', 'Pharmacy'),
    ('clinic', 'Clinic'),
    ('commercial building', 'Commercial Building'),
    ('commercial land', 'Commercial Land'),
    ('agricultural', 'Agricultural'),
    ('warehouse', 'Warehouse'),
    ('other commercial', 'Other Commercial'),
    ('garage', 'Garage'),
    ('garage', 'Garage'),
    ]
    countries = [
        ('EG', 'Egypt'),
    ]
    governorates = [
        ('Cairo', 'Cairo'),
        ('Alexandria', 'Alexandria'),
        ('Giza', 'Giza'),
        ('Qalyubia', 'Qalyubia'),
        ('Dakahlia', 'Dakahlia'),
        ('Sharqia', 'Sharqia'),
        ('Gharbia', 'Gharbia'),
        ('Monufia', 'Monufia'),
        ('Kafr El Sheikh', 'Kafr El Sheikh'),
        ('Damietta', 'Damietta'),
        ('Port Said', 'Port Said'),
        ('Ismailia', 'Ismailia'),
        ('Suez', 'Suez'),
        ('Aswan', 'Aswan'),
        ('Luxor', 'Luxor'),
        ('Red Sea', 'Red Sea'),
        ('Matrouh', 'Matrouh'),
        ('North Sinai', 'North Sinai'),
        ('South Sinai', 'South Sinai'),
        ('Faiyum', 'Faiyum'),
        ('Beni Suef', 'Beni Suef'),
        ('Minya', 'Minya'),
        ('Assiut', 'Assiut'),
        ('Sohag', 'Sohag'),
        ('Qena', 'Qena'),
        ('New Valley', 'New Valley'),
        ('Damietta', 'Damietta')
    ]
    sale_rent = [
        ('sale','Sale'),
        ('rent','Rent')
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,unique=False,blank=False)
    description = models.TextField(blank=False)
    property_type = models.CharField(max_length=11, choices=property_type,blank=False)
    price = models.IntegerField()
    location = models.CharField(max_length=255,blank=False)
    listed_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=2, choices=countries,blank=False)
    governorate = models.CharField(max_length=20,blank=False, choices=governorates)
    city = models.CharField(max_length=50,blank=False)
    street = models.CharField(max_length=50)
    commercial = models.CharField(max_length=20,blank=False, choices=commercial_type)
    is_sale = models.CharField(max_length=4,blank=False, choices=sale_rent)
    image = models.ImageField(upload_to='property/images', blank=False)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    ads_id = models.ForeignKey('ads.Ads', on_delete=models.CASCADE, related_name='property_ids')



