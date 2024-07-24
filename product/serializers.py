from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Category
        

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        fields = ('id', 'name', 'slug', 'price', 'wage', 'weight', 'code', 'cutie', 'color', 'stock', 'image', 'thumbnail', 'date_added', 'category')
        model = Product
