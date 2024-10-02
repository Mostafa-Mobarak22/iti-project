from unittest.result import failfast

from django.shortcuts import redirect

from ..models import *
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
import jwt,datetime
from django.urls import reverse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view
from django.utils.http import urlsafe_base64_decode , urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,DjangoUnicodeDecodeError
from django.core.mail import send_mail,EmailMessage
import base64
# from django.contrib.auth.models import User as token
@api_view(['GET'])
def user_details(request,id):
    if request.method == 'GET':
        if User.objects.filter(pk=id).exists():
            user = User.objects.get(pk=id)
            user_json = UserSerializer(user)
            return Response(data=user_json.data, status=200)
        else:
            return Response({"error_message": "account not found"})
    return Response({"error_message": "invalid method"})

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
        print(request)
        print(get_current_site(request).domain)
        filterable_fields = ['username','email',"phone"]
        fields = {key: request.data[key] for key in filterable_fields if key in request.data}
        for field in fields :
            field_user = {field:fields[field]}
            if User.objects.filter(**field_user).exists():
                return Response({"error_message": "This user already exists"})
        if user.is_valid():
            user.save()
            if send_email(request.data['email'],request.data['user_name'],request):
                return Response({"error_message": "Incorrect Email"})
            else :
                # user.save()
                print(get_current_site(request).domain)
                return Response({"success_message": "Check Your Mail to Activate Your Account"},status=status.HTTP_201_CREATED)
        else:
            return Response(user.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response({"error_message": "invalid method"})

@api_view(['PUT'])
def update_user(request,id):
    if User.objects.filter(pk=id).exists():
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
    else:
        return Response({"error_message": "account not found"})

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
    # print(request.data)
    print(request.FILES)
    user = User.objects.get(pk=id)
    if request.method == 'PATCH':
        user_json = UserSerializer(user,data=request.data,partial=True)
        # print(request.data)
        # print(user_json)
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
                if User.objects.get(user_name=request.data['user_name']).is_active:
                    get_user = User.objects.get(user_name=request.data['user_name'])
                    payload = {
                        'id' : get_user.id,
                        'exp':datetime.datetime.utcnow()+datetime.timedelta(hours=24),
                        'iat':datetime.datetime.utcnow(),
                    }
                    token = jwt.encode(payload,'secret',algorithm='HS256')
                    return Response({"token":token,"user_name":request.data['user_name']})
                else:
                    return Response({"not_active": "your account not active check your mail"})
            else:
                return Response({"error": "password not correct"})
        else:
            return Response({"error": "user_name not correct"})
    return Response({"error": "invalid method"})
def encode_data (user_name):
    user_info = f"{user_name}".encode('utf-8')
    encoded_data = base64.urlsafe_b64encode(user_info).decode('utf-8')
    return encoded_data
def decode_data(encoded_data):
    decoded_data = base64.urlsafe_b64decode(encoded_data).decode('utf-8')
    user_name = decoded_data
    return user_name


def activate_account(request, encoded_data):
    try:
        print(request)
        username = decode_data(encoded_data)
        print(username)
        user = User.objects.get(user_name=username)
        print(user)
        if user.is_active:
            return redirect('login_user')
        user.is_active = True
        user.save()
        return redirect('http://localhost:5173/login')
    except (User.DoesNotExist, ValueError):
        return Response('Invalid activation link or user does not exist.')
def send_email(email, user_name,request):
    print(user_name)
    encoded_data = encode_data(user_name)
    activation_link = f"{get_current_site(request).domain}/user/activate/{encoded_data}/"
    email_subject = "Activate Your Account on Buyout"
    email_body = activation_link
    email_massege = EmailMessage(
    email_subject,
    email_body,
    "buyout71@gmail.com",
    [email],
    )
    try:
        email_massege.send(fail_silently=False)
        return False
    except Exception as e:
        return "Incorrect Email"