from rest_framework import serializers
from django.core.validators import EmailValidator
from rest_framework.validators import UniqueValidator
from ..models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'image': {'required': False, 'allow_null': True},
            'country': {'required': False, 'allow_null': True},
            'city': {'required': False, 'allow_null': True},
            'street': {'required': False, 'allow_null': True},
            'address': {'required': False, 'allow_null': True},
            'another_phone': {'required': False, 'allow_null': True},
            'register_photo': {'required': False, 'allow_null': True},
            'is_company': {'required': False},
            'is_active': {'required': False},
            'property_ids': {'required': False, 'allow_null': True},
            "wish": {'required': False},
            "member_duration": {'required': False},
            "member_time": {'required': False}
        }
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'image': {'required': False, 'allow_null': True},
            'phone': {'required': False, 'allow_null': True},
            'email': {'required': False, 'allow_null': True},
            'country': {'required': False, 'allow_null': True},
            'city': {'required': False, 'allow_null': True},
            'street': {'required': False, 'allow_null': True},
            'address': {'required': False, 'allow_null': True},
            'another_phone': {'required': False, 'allow_null': True},
            'register_photo': {'required': False, 'allow_null': True},
            'is_company': {'required': False},
            'property_ids': {'required': False, 'allow_null': True},
            "wish":{'required': False}
        }

class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = '__all__'
        extra_kwargs ={
            'data':{'required': False}
        }