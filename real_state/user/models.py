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
    user_name = models.CharField(max_length=25,unique=True,blank=False)
    image = models.ImageField(upload_to='user/images/profile/',null=True)
    email = models.CharField(max_length=254,unique=True, validators=[EmailValidator()],blank=False)
    password = models.CharField(max_length=50,blank=False)
    country = models.CharField(max_length=2, choices=countries,null=True)
    city = models.CharField(max_length=50,null=True)
    street = models.CharField(max_length=50,null=True)
    address = models.TextField(null=True,default='')
    phone = models.CharField(blank=False,max_length=11,unique=True)
    another_phone = models.CharField(max_length=11,null=True)
    register_photo = models.ImageField(upload_to='user/images/register/',null=True)
    is_company = models.BooleanField(null=True)
    property_ids = models.ForeignKey('property.Property',on_delete=models.CASCADE,related_name='user_id',null=True)



    def __str__(self):
        return self.user_name
