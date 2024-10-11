
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.db import models
from property.models import *
from django.core.validators import MinLengthValidator
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=25,unique=True,blank=False,validators=[MinLengthValidator(5)])
    image = models.ImageField(upload_to='user/images/profile/',null=True,blank=True)
    email = models.CharField(max_length=254,unique=True, validators=[EmailValidator()],blank=False)
    password = models.CharField(max_length=50,blank=False,validators=[MinLengthValidator(8)])
    city = models.CharField(max_length=25,null=True,validators=[MinLengthValidator(3)],blank=True)
    street = models.CharField(max_length=50,null=True,validators=[MinLengthValidator(5)],blank=True)
    address = models.TextField(null=True,default='',blank=True)
    phone = models.CharField(blank=False,max_length=11,unique=True,validators=[MinLengthValidator(11)])
    another_phone = models.CharField(max_length=11,null=True,validators=[MinLengthValidator(11)],blank=True)
    register_photo = models.ImageField(upload_to='user/images/register/',null=True,blank=True)
    is_company = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    member_duration = models.IntegerField(blank=True, null=True)
    member_time = models.DateTimeField(null=True, blank=True)
    wish = models.IntegerField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name

class Wish(models.Model):
    property_ids = models.JSONField(blank=True, null=True,default=[])
    user_id = models.IntegerField(blank=False, null=False)
    data = models.JSONField(blank=True, null=True,default=[])