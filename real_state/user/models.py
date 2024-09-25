from importlib.metadata import requires
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.db import models
from property.models import *
# Create your models here.
class User(models.Model):
    countries = [
    ('EG', 'Egypt'),
]

    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=25,unique=True,blank=False,null=True)
    image = models.ImageField(upload_to='user/images/profile/',null=True,blank=True)
    email = models.CharField(max_length=254,unique=True, validators=[EmailValidator()],blank=False)
    password = models.CharField(max_length=50,blank=False)
    country = models.CharField(max_length=2, choices=countries,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    street = models.CharField(max_length=50,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    phone = models.CharField(blank=False,max_length=11)
    another_phone = models.CharField(max_length=11,null=True,blank=True)
    register_photo = models.ImageField(upload_to='user/images/register/',null=True,blank=True)
    is_company = models.BooleanField(null=True,blank=True)
    property_ids = models.ForeignKey('property.Property',on_delete=models.CASCADE,related_name='user_id',null=True,blank=True)


    def __str__(self):
        return self.user_name
