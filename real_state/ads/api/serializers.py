from rest_framework import serializers
from ads.models import Ads

class Adserializer(serializers.ModelSerializer):
   class Meta:
        model = Ads
        fields = '__all_