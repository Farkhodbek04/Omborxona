from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import CategorySerializer, ProductSerializer, UnitSerializer

class CategoryCRUDview(viewsets.ModelViewSet):

    """ This is CategoryCRUDview class that performs CRUD operations."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UnitCRUDview(viewsets.ModelViewSet):
    
    """ This is CategoryCRUDview class that performs CRUD operations."""

    queryset = Unit.objects.all()
    serializer_class = UnitSerializer