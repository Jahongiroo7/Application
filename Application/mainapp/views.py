from django.shortcuts import render

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Worker, Application, Category
from .serializers import ApplicationSerializer, CategorySerializer, WorkerSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.filter(status='qabul_qilingan')
    serializer_class = ApplicationSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=True)
    serializer_class = CategorySerializer

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.filter(status=True)
    serializer_class = WorkerSerializer
