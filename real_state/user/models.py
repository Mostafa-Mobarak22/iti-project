from importlib.metadata import requires
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.db import models
from property.models import *
from django.core.validators import MinLengthValidator
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.
class User(models.Model):
    countries = [
    ('EG', 'Egypt'),
]

    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=25,unique=True,blank=False,validators=[MinLengthValidator(5)])
    image = models.ImageField(upload_to='user/images/profile/',null=True)
    email = models.CharField(max_length=254,unique=True, validators=[EmailValidator()],blank=False)
    password = models.CharField(max_length=50,blank=False,validators=[MinLengthValidator(8)])
    country = models.CharField(max_length=2, choices=countries,null=True)
    city = models.CharField(max_length=50,null=True)
    street = models.CharField(max_length=50,null=True)
    address = models.TextField(null=True,default='')
    phone = models.CharField(blank=False,max_length=11,unique=True,validators=[MinLengthValidator(11)])
    another_phone = models.CharField(max_length=11,null=True,validators=[MinLengthValidator(11)])
    register_photo = models.ImageField(upload_to='user/images/register/',null=True)
    is_company = models.BooleanField(default=False)
    property_ids = models.ForeignKey('property.Property',on_delete=models.CASCADE,related_name='user_id',null=True)

    def get_tokens_for_user(self):
        token = RefreshToken.for_user(self)
        return {
            'token': str(token),
            'access': str(token.access_token),
        }

    def __str__(self):
        return self.user_name
