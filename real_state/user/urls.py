from django.urls import path
from .api.views import *
urlpatterns = [
    path('get/<int:id>/',user_details),
    path('',all_user),
    path('add/',add_user),
    path('update/<int:id>/',update_user),
    path('delete/<int:id>/',delete_user),
    path('<int:id>/',patch_user),
    path('massage/',send_massage),
    path('login/',login_user,name="login_user"),
    path('activate/<str:encoded_data>/', activate_account, name='activate_account'),
]