from rest_framework import serializers
from django.core.validators import EmailValidator
class UserSerializer(serializers.Serializer):
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

    id = serializers.IntegerField(read_only=True)
    user_name = serializers.CharField(max_length=25,  allow_blank=False)
    image = serializers.ImageField()
    email = serializers.CharField(max_length=254,  validators=[EmailValidator()])
    password = serializers.CharField(max_length=50, allow_blank=False)
    country = serializers.ChoiceField(countries,allow_blank=False)
    city = serializers.CharField(max_length=50, allow_blank=False)
    street = serializers.CharField(max_length=50, allow_blank=False)
    address = serializers.CharField(allow_blank=False)
    phone = serializers.CharField(allow_blank=False, max_length=11)
    another_phone = serializers.CharField(max_length=11)
    register_photo = serializers.ImageField()
    is_company = serializers.BooleanField()