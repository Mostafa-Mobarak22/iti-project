from rest_framework import serializers
from property.models import Property, PropertyImage
from user.api.serializers import UserSerializer
from user.models import User


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)  # Get full user details in responses
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    images = serializers.SerializerMethodField()
    class Meta:
        model = Property
        fields = '__all__'
    def get_images(self, obj):
        images = PropertyImage.objects.filter(property_id=obj)
        return [image.image.url for image in images]
    def create(self, validated_data):
        user = validated_data.pop('user')
        property_instance = Property.objects.create(user_id=user, **validated_data)
        return property_instance
