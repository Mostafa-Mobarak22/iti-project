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
    path('confirm/',confirm_email),
    path('wishlist/',add_data),
    path('password/',change_password),
    path('changepassword/<str:encoded_data>/',get_password, name='get_password'),
    path('savepassword/',save_password, name='save_password'),
    path('wishlist/<int:id>/',get_wishlist),
    path('login/',login_user,name="login_user"),
    path('activate/<str:encoded_data>/', activate_account, name='activate_account'),
]