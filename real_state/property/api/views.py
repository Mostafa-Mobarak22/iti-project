from rest_framework import viewsets
from rest_framework.decorators import api_view
from property.models import Property, PropertyImage
from .serializers import PropertySerializer, PropertyImageSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        property_serializer = PropertySerializer(data=request.data)
        property_serializer.is_valid(raise_exception=True)
        property_instance = property_serializer.save()

        # Now handle multiple image uploads
        images = request.FILES.getlist('image')  # 'image' should match the file input name
        print(request.FILES,images)
        for image in images:
            PropertyImage.objects.create(property_id=property_instance, image=image)

        # Return a response after successfully creating the property and images
        return Response(property_serializer.data, status=status.HTTP_201_CREATED)

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

@api_view(["POST"])
def same_properties_type(request):
    if request.method == 'POST':
        property = Property.objects.filter(commercial=request.data["commercial"])
        property_json = PropertySerializer(property,many=True)
        return Response(data=property_json.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def search(request):
    if request.method == 'POST':
        properties = Property.objects.filter(is_published=True)
        if(request.data["buy"]):
            properties = properties.filter(is_sale=request.data["buy"])
        if(request.data["bed"]):
            properties = properties.filter(bed=request.data["bed"])
        if(request.data["bath"]):
            properties = properties.filter(bath=request.data["bath"])
        if(request.data["usage"]):
            properties = properties.filter(property_type=request.data["usage"])
        if(request.data["residential"]):
            properties = properties.filter(commercial=request.data["residential"])
        elif(request.data["commercial"]):
            properties = properties.filter(commercial=request.data["commercial"])
        if(request.data["maxarea"]):
            properties = properties.filter(area__lte=request.data["maxarea"])
        elif(request.data["minarea"]):
            properties = properties.filter(area__gte=request.data["minarea"])
        if(request.data["maxprice"]):
            properties = properties.filter(price__lte=request.data["maxprice"])
        elif(request.data["minprice"]):
            properties = properties.filter(price__gte=request.data["minprice"])
        if(request.data["search"]):
            search = request.data.get('search', '')
            properties = properties.filter(location__icontains=search)
        property_json = PropertySerializer(properties, many=True)
        return Response(data=property_json.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)