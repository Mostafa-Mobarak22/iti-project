from ..models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view

@api_view(['GET'])
def user_details(request,id):
    if request.method == 'GET':
        user = User.objects.get(pk=id)
        user_json = UserSerializer(user)
        return Response(user_json.data)
    return Response({"error message": "xxxxxx"})

def users_details(request,id):
    return "Response(user_json.data)"


