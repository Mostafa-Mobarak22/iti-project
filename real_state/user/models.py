from importlib.metadata import requires
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.db import models
from property.models import *
# Create your models here.
class User(models.Model):
    countries = [
    ('SA', 'Saudi Arabia'),
    ('AE', 'United Arab Emirates'),
    ('EG', 'Egypt'),
    ('IQ', 'Iraq'),
    ('JO', 'Jordan'),
    ('MA', 'Morocco'),
    ('KW', 'Kuwait'),
    ('QA', 'Qatar'),
    ('OM', 'Oman'),
    ('DZ', 'Algeria'),
]

    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=25,unique=True,blank=False)
    image = models.ImageField(upload_to='user/images/profile/')
    email = models.CharField(max_length=254,unique=True, validators=[EmailValidator()])
    password = models.CharField(max_length=50,blank=False)
    country = models.CharField(max_length=2, choices=countries,blank=False)
    city = models.CharField(max_length=50,blank=False)
    street = models.CharField(max_length=50,blank=False)
    address = models.TextField(blank=False)
    phone = models.CharField(blank=False,max_length=11)
    another_phone = models.CharField(max_length=11)
    register_photo = models.ImageField(upload_to='user/images/register/')
    is_company = models.BooleanField()
    property_ids = models.ForeignKey('property.Property',on_delete=models.CASCADE,related_name='user_id')

