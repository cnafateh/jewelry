from django.urls import path
from .views import CategoryList, ProductList, ProductDetail

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('products/', ProductList.as_view()),
    path('products/<str:category_slug>/', ProductDetail.as_view()),
]
