from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .views import CategoryViewSet, ApplicationViewSet,WorkerViewSet

router = routers.DefaultRouter()
router.register(r"application", ApplicationViewSet)
router.register(r"worker", WorkerViewSet)
router.register(r"category", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]