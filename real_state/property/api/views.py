# property/views.py
from rest_framework import viewsets
from property.models import Property, PropertyImage
from rest_framework.response import Response
from rest_framework import status
from .serializers import PropertySerializer, PropertyImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser
class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyImageViewSet(viewsets.ModelViewSet):

    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer

