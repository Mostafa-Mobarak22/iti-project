from ..models import *
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
import jwt,datetime
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view
# from django.contrib.auth.models import User as token
@api_view(['GET'])
def user_details(request,id):
    if request.method == 'GET':
        user = User.objects.get(pk=id)
        user_json = UserSerializer(user)
        return Response(data=user_json.data, status=200)
    return Response({"error message": "not found user"})

@api_view(['GET'])
def all_user(request):
    if request.method == 'GET':
        user = User.objects.all()
        user_json = UserSerializer(user,many=True)
        return Response(data=user_json.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_user(request):
    if request.method == 'POST':
        user = UserSerializer(data=request.data)
        filterable_fields = ['username','email',"phone"]
        fields = {key: request.data[key] for key in filterable_fields if key in request.data}
        for field in fields :
            field_user = {field:fields[field]}
            if User.objects.filter(**field_user).exists():
                return Response({"error message": "This user already exists"})
        if user.is_valid():
            user.save()
            return Response({"success message": "User Is Add"},status=status.HTTP_201_CREATED)
        else:
            return Response(user.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response({"error message": "invalid method"})

@api_view(['PUT'])
def update_user(request,id):
    user = User.objects.get(pk=id)
    user_json = UserSerializer(instance=user,data=request.data)
    filterable_fields = ['username', 'email', "phone"]
    fields = {key: request.data[key] for key in filterable_fields if key in request.data}
    for field in fields:
        field_user = {field: fields[field]}
        if User.objects.filter(**field_user).exists():
            return Response({"error message": "This user already exists"})
    if user_json.is_valid():
        user_json.save()
        return Response(user_json.data)
    else:
        return Response(user_json.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_user(request,id):
    user=User.objects.filter(id=id)
    if(len(user)>0):
        user.delete()
        return Response(data={'msg':'deleted'})
    return Response({'msg':'user not found'})

@api_view(['PATCH'])
def patch_user(request,id):
    parser_classes = (MultiPartParser, FormParser)
    print(request.data)
    print(request.FILES)
    user = User.objects.get(pk=id)
    if request.method == 'PATCH':
        user_json = UserSerializer(user,data=request.data,partial=True)
        # filterable_fields = ['username','email',"phone"]
        # fields = {key: request.data[key] for key in filterable_fields if key in request.data}
        # for field in fields :
        #     field_user = {field:fields[field]}
        #     if User.objects.filter(**field_user).exists():
        #         return Response({"error message": "This data already exists"})
        print(request.data)
        print(user_json)
        if user_json.is_valid():
            user_json.save()
            return Response(user_json.data)
        return Response(user_json.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        user = LoginSerializer(data=request.data)
        if User.objects.filter(user_name=request.data['user_name']).exists() :
            if User.objects.get(user_name=request.data['user_name']).password ==request.data['password']:
                get_user = User.objects.get(user_name=request.data['user_name'])
                payload = {
                    'id' : get_user.id,
                    'exp':datetime.datetime.utcnow()+datetime.timedelta(hours=24),
                    'iat':datetime.datetime.utcnow(),
                }
                token = jwt.encode(payload,'secret',algorithm='HS256')
                return Response({"token":token,"success":request.data['user_name']})
            else:
                return Response({"error": "password not correct"})
        else:
            return Response({"error": "user_name not correct"})
    return Response({"error": "invalid method"})