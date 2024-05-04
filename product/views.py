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
    
    def delete(self, request):
            # Check if the user is an accountant
            if request.user.position != 0:  # Assuming 0 represents the position of an accountant
                return Response({"message": "You do not have permission to perform this action"}, status=status.HTTP_403_FORBIDDEN)
            
            user_id = request.data.get('user_id')  # Assuming user_id is sent in the request data
            user = get_object_or_404(User, id=user_id)
            user.delete()
            return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
