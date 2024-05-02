from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


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
