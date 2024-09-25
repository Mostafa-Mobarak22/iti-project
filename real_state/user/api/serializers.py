from rest_framework import serializers
from django.core.validators import EmailValidator
class UserSerializer(serializers.Serializer):
    countries = [
        ('EG', 'Egypt'),
    ]

    id = serializers.IntegerField(read_only=True)
    user_name = serializers.CharField(max_length=25)
    image = serializers.ImageField(required=False)
    email = serializers.CharField(max_length=254,validators=[EmailValidator()])
    password = serializers.CharField(max_length=50)
    country = serializers.ChoiceField(countries,required=False)
    city = serializers.CharField(max_length=50,required=False)
    street = serializers.CharField(max_length=50,required=False)
    address = serializers.CharField(required=False)
    phone = serializers.CharField(max_length=11)
    another_phone = serializers.CharField(max_length=11,required=False)
    register_photo = serializers.ImageField(required=False)
    is_company = serializers.BooleanField(required=False)