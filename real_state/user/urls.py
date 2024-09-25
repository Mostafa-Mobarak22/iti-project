from django.urls import path
from .api.views import *
urlpatterns = [
    path('getuser/<int:id>/',user_details),
    path('',all_user),
]