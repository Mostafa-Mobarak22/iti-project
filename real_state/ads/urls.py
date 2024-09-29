from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.views import Adsviwses

router = DefaultRouter()
router.register(r'ads', Adsviwses)

urlpatterns = [
    path('', include(router.urls)),
]
