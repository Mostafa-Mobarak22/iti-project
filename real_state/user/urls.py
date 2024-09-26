from django.urls import path
from .api.views import *
urlpatterns = [
    path('get/<int:id>/',user_details),
    path('',all_user),
    path('add/',add_user),
    path('update/<int:id>/',update_user),
    path('delete/<int:id>/',delete_user),
    path('<int:id>/',patch_user),
]