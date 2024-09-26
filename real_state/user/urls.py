from django.urls import path
from .api.views import *
urlpatterns = [
    path('get/user/<int:id>/',user_details),
    path('',all_user),
    path('add/user/',add_user),
    path('update/user/<int:id>',update_user),
    path('delete/user/<int:id>',delete_user),
]