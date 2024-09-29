from rest_framework import viewsets
from ads.models import Ads,
from .serializers import Adserializer


class Adsviwses(viewsets.ModelViewSet):
    queryset = Ads.objects.all()
    serializer_class = Adserializer