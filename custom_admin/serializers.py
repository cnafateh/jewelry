from rest_framework import serializers
from product.models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# یک نمونه برای پست کردن
# {
#     "category": 1,
#     "name": "Gold Necklace",
#     "slug": "gold-necklace",
#     "price": "2500.00",
#     "wage": "150.00",
#     "weight": "10.50",
#     "code": "GN123",
#     "cutie": 1,
#     "color": "Gold",
#     "stock": true,
#     "image": null,
#     "thumbnail": null
# }

# نمونه JSON برای به‌روزرسانی محصول (PUT):
# {
#     "name": "Updated Necklace",
#     "price": "2600.00"
# }

# نمونه JSON برای پست کردن دسته‌بندی:
# {
#     "name": "Necklaces",
#     "slug": "necklaces"
# }
