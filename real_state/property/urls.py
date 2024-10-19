# property/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.views import PropertyViewSet, PropertyImageViewSet,user,newest_properties,same_properties_type,search

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'property-images', PropertyImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/<int:user_id>/',user),
    path('newest/',newest_properties),
    path('same/',same_properties_type),
    path('search/',search),
]
