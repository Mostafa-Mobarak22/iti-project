from django.db import models
from django.core.validators import MinLengthValidator ,MaxValueValidator, MinValueValidator
from ads.models import *
from user.models import *
# Create your models here.
class Property(models.Model):
    property_type = [
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
    ]
    commercial_type = [
    ('Office', 'Office'),
    ('Retail', 'Retail'),
    ('Restaurant', 'Restaurant'),
    ('Pharmacy', 'Pharmacy'),
    ('Clinic', 'Clinic'),
    ('Commercial Building', 'Commercial Building'),
    ('Commercial Land', 'Commercial Land'),
    ('Agricultural', 'Agricultural'),
    ('Warehouse', 'Warehouse'),
    ('Garage', 'Garage'),
    ('Other Commercial', 'Other Commercial'),
    ]
    countries = [
        ('Egypt', 'Egypt'),
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
    title = models.CharField(max_length=100,unique=False,blank=False ,validators=[MinLengthValidator(5)])
    description = models.TextField(blank=False)
    property_type = models.CharField(max_length=11, choices=property_type,blank=False)
    price = models.IntegerField(blank=False)
    is_published = models.BooleanField(default=False)
    bed = models.IntegerField(null=True,default=1)
    bath = models.IntegerField(null=True,default=1)
    location = models.CharField(max_length=150,blank=False , validators=[MinLengthValidator(10)])
    listed_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=5, choices=countries,blank=False)
    governorate = models.CharField(max_length=20,blank=False, choices=governorates)
    city = models.CharField(max_length=50,blank=False,validators=[MinLengthValidator(4)])
    street = models.CharField(max_length=50,validators=[MinLengthValidator(5)])
    commercial = models.CharField(max_length=20,blank=False, choices=commercial_type)
    is_sale = models.CharField(max_length=4,blank=False, choices=sale_rent,default="sale")
    area = models.DecimalField(max_digits=7, decimal_places=1,blank=False)
    user_id = models.ForeignKey("user.User",blank=False,related_name='properties',on_delete=models.CASCADE)
    ads_id = models.ForeignKey('ads.Ads', on_delete=models.CASCADE, related_name='property_ids',null=True,blank=True)
    image = models.ImageField(upload_to='property/images', blank=False)


    def __str__(self):
        return self.title

class PropertyImage(models.Model):
    property_id = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property/images', blank=False)

