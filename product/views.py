from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import CategorySerializer, ProductSerializer, UnitSerializer, UserSerializer

class CategoryCRUDview(viewsets.ModelViewSet):

    """ This is CategoryCRUDview class that performs CRUD operations."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UnitCRUDview(viewsets.ModelViewSet):
    
    """ This is CategoryCRUDview class that performs CRUD operations."""

    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class SetStorekeeperView(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            # Retrieve a specific user by ID
            user = get_object_or_404(User, id=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            # Get all users
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Check if the user is an accountant
            if request.user.position != 0:  # Assuming 0 represents the position of an accountant
                return Response({"message": "You do not have permission to perform this action"}, status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
            # Check if the user is an accountant
            if request.user.position != 0:  # Assuming 0 represents the position of an accountant
                return Response({"message": "You do not have permission to perform this action"}, status=status.HTTP_403_FORBIDDEN)
            
            user = get_object_or_404(User, id=pk)
            user.delete()
            return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data)
        except user.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProductCRUDView(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            try:
                queryset = Product.objects.get(pk=pk)
                serializer = ProductSerializer(queryset)
                return Response(serializer.data)
            except Product.DoesNotExist:
                return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Your product has been created successfuly!"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product, data=request.data)
        except Product.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            item = Product.objects.get(pk=pk)
            item.delete()
            return Response({"message": "The product has been deleted."})
        except item.DoesNotExist:
            return Response({"message": "Product does not exist!"})
        