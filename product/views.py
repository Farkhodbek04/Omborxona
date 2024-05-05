from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import CategorySerializer, ProductSerializer, UnitSerializer, UserSerializer, ProductInputSerializer, ProductOutputSerializer

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
                return Response({"xabar": "Sizga omborchi yaratishga ruxsat yo'q."}, status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
            # Check if the user is an accountant
            if request.user.position != 0:  # Assuming 0 represents the position of an accountant
                return Response({"xabar": "Sizga o'chirishga ruxsat yo'q."}, status=status.HTTP_403_FORBIDDEN)
            
            user = get_object_or_404(User, id=pk)
            user.delete()
            return Response({"xabar": "Omborchi o'chirildi."}, status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data)
        except User.DoesNotExist:
            return Response({"xabar": "omborchi topilmadi."}, status=status.HTTP_404_NOT_FOUND)
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
                return Response({"xabar": "Maxsulot topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        else:
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar": "Maxsulot yaratildi!"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product, data=request.data)
        except Product.DoesNotExist:
            return Response({"xabar": "Maxsulot topilmadi"}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar": "Maxsulot tahrirlandi"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            item = Product.objects.get(pk=pk)
            item.delete()
            return Response({"xabar": "Maxsulot o'chirildi."})
        except Product.DoesNotExist:
            return Response({"xabar": "Maxsulot topilmadi!"})
        

class ProductInputView(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            try:
                item = ProductInput.objects.get(pk=pk)
                serializer = ProductInputSerializer(item)
                return Response(serializer.data)
            except ProductInput.DoesNotExist:
                return Response({"xabar": "Kirim topilmadi!"})
        else:
            items = ProductInput.objects.all()
            serializer = ProductInputSerializer(items, many=True)
            return(serializer.data)
        
    def post(self, request):
        serializer = ProductInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar": "Yangi Kirim yaratildi!"})
        else:
            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
        try:
            item = ProductInput.objects.get(pk=pk)
            serializer = ProductInputSerializer(item, data=request.data)
        except ProductInput.DoesNotExist:
            return Response({"xabar": "Kirim topilmadi"})
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar": "Kirim taxrirlandi!"})
        return Response(serializer.errors)

    def delete(self, request, pk):
        try:
            item = ProductInput.objects.get(pk=pk)
            item.delete()
            return Response({"xabar": "Kirim o'chirildi!"})
        except ProductInput.DoesNotExist:
            return Response({"xabar": "Kirim topilmadi!"})


class ProductOutputView(APIView):

    def get(self, request, pk=None):
        if pk:
            try:
                item = ProductOutput.objects.get(pk=pk)
                serializer = ProductOutputSerializer(item)
                return Response(serializer.data)
            except ProductOutput.DoesNotExist:
                return Response({"xabar": "Chiqim topilmadi."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            items = ProductOutput.objects.all()  
            serializer = ProductOutputSerializer(items, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductOutputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar": "Yangi chiqim yaratildi!"})
        else:
            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
        try:
            item = ProductOutput.objects.get(pk=pk)
            serializer = ProductOutputSerializer(item, data=request.data)
        except ProductOutput.DoesNotExist:
            return Response({"xabar": "Chiqim topilmadi."}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar": "Chiqim taxrirlandi!"})
        else:
            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            item = ProductOutput.objects.get(pk=pk)
            item.delete()
            return Response({"xabar": "Chiqim o'chirildi!"})
        except ProductOutput.DoesNotExist:
            return Response({"xabar": "Chiqim topilmadi."}, status=status.HTTP_400_BAD_REQUEST)
        