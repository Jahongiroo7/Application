from django.shortcuts import render

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, pagination
from .models import Worker, Application, Category
from .serializers import ApplicationSerializer, CategorySerializer, WorkerSerializer

class our_pagination(pagination.PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.filter(status='qabul_qilingan')
    serializer_class = ApplicationSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=True)
    serializer_class = CategorySerializer

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.filter(status=True)
    serializer_class = WorkerSerializer
    pagination_class = our_pagination