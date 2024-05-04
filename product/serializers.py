from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
   class Meta:
        model = User
        fields = ['id','username', 'position'] 



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id','name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInput
        fields = '__all__'


class ProductOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOutput
        fields = '__all__'
