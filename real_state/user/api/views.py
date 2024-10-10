from unittest.result import failfast

from django.shortcuts import redirect, get_object_or_404

from property.api.serializers import PropertySerializer
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
                add_wish(User.objects.get(user_name=request.data['user_name']).id)
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
    print(request.data)
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
                    return Response({"token":token,"user_name":request.data['user_name'],"id":User.objects.get(user_name=request.data['user_name']).id})
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

@api_view(['POST'])
def send_massage(request):
    if request.method == "POST":
        name = request.data["name"]
        email = request.data['email']
        massage = request.data['massage']
        email_subject = f"{name} Want More Information About Your Property"
        email_body = massage
        email_massage = EmailMessage(
        email_subject,
        email_body,
        "buyout71@gmail.com",
        [email],
        )
        try:
            email_massage.send(fail_silently=False)
            return Response({"success_massage":"We will contact you as soon as possible"})
        except Exception as e:
            return Response({"error_massage":"There is a problem now, you can try again later"})
    else:
        return Response({"error": "invalid method"})

def add_wish(id):
    new_wish = Wish.objects.create(
        user_id = id
    )
    new_wish.save()
@api_view(["POST"])
def add_data(request):
    wishlist = Wish.objects.get(user_id=request.data["user_id"])
    property_id = wishlist.property_ids
    data = wishlist.data
    if request.data["property_ids"] in property_id:
        for x in property_id:
            if request.data["property_ids"] == x:
                property_id.remove(x)
        for x in data:
            print(x)
            if request.data["property_ids"] == x["id"]:
                data.remove(x)
        wishlist.data = data
        wishlist.property_ids = property_id
        wishlist.save()
        return Response({"error": "this property deleted"})
    else:
        property_id.append(request.data["property_ids"])
        property = Property.objects.get(id=request.data["property_ids"])
        new_data = {
            "id": property.id,
            "title": property.title,
            "description": property.description,
            "property_type": property.property_type,
            "price": property.price,
            "is_published": property.is_published,
            "bed": property.bed,
            "bath": property.bath,
            "location": property.location,
            "listed_date": property.listed_date.isoformat(),
            "country": property.country,
            "governorate": property.governorate,
            "city": property.city,
            "street": property.street,
            "commercial": property.commercial,
            "is_sale": property.is_sale,
            "area": property.area.is_normal(),
            "image": property.image.url if property.image else None,
        }
        data.append(new_data)
        wishlist.data = data
        wishlist.property_ids = property_id
        wishlist.save()

        return Response({"success": "property added to your wishlist"})

@api_view(["GET"])
def get_wishlist(request,id):
    if request.method == 'GET':
        if Wish.objects.filter(user_id=id).exists():
            wish = Wish.objects.filter(user_id=id)
            wish_json = WishListSerializer(wish,many=True)
            return Response(data=wish_json.data, status=200)
        else:
            return Response({"error_message": "your wishlist is empty"})
    return Response({"error_message": "invalid method"})
