from rest_framework.permissions import IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from product.models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

# View for creating Products (POST only)
class ProductCreateAPIView(APIView):

    permission_classes = [IsAdminUser]
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View for updating Products (PUT only)
class ProductUpdateAPIView(APIView):

    permission_classes = [IsAdminUser]
    def put(self, request, pk, *args, **kwargs):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View for creating Categories (POST only)
class CategoryCreateAPIView(APIView):

    permission_classes = [IsAdminUser]
    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View for updating Categories (PUT only)
class CategoryUpdateAPIView(APIView):

    permission_classes = [IsAdminUser]
    def put(self, request, pk, *args, **kwargs):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
