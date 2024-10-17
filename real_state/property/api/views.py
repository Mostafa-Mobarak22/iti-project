# property/views.py
from rest_framework import viewsets
from rest_framework.decorators import api_view

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

@api_view(["GET"])
def user(request,user_id):
    user_properties = Property.objects.filter(user_id=user_id)
    user_properties_json = PropertySerializer(user_properties,many=True)
    return Response(data=user_properties_json.data, status=status.HTTP_201_CREATED)

@api_view(["GET"])
def newest_properties(request):
    if request.method == 'GET':
        property = Property.objects.filter(is_published=True).order_by('-id')[:6]
        property_json = PropertySerializer(property,many=True)
        return Response(data=property_json.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)