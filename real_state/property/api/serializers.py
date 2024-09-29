from rest_framework import serializers
from property.models import Property, PropertyImage

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'  # يمكنك تحديد الحقول التي تريدها بدلاً من ذلك

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = '__all__'  # يمكنك تحديد الحقول التي تريدها بدلاً من ذلك
