from ..models import *
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view

@api_view(['GET'])
def user_details(request,id):
    if request.method == 'GET':
        user = User.objects.get(pk=id)
        user_json = UserSerializer(user)
        return Response(data=user_json.data, status=200)
    return Response({"error message": "xxxxxx"})

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
        if user.is_valid():
            user.create(User,user.user_name,user.email,user.password,user.phone)
            return Response({"success message": "User Is Add"},status=status.HTTP_201_CREATED)
        else:
            print('ll')
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response({"error message": "xxxxxx"})




