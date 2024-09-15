from django.urls import path
from .views import ProductCreateAPIView, ProductUpdateAPIView, CategoryCreateAPIView, CategoryUpdateAPIView

urlpatterns = [
    # Product-related URLs
    path('create-product/', ProductCreateAPIView.as_view(), name='create-product'),
    path('update-product/<int:pk>/', ProductUpdateAPIView.as_view(), name='update-product'),

    # Category-related URLs
    path('create-category/', CategoryCreateAPIView.as_view(), name='create-category'),
    path('update-category/<int:pk>/', CategoryUpdateAPIView.as_view(), name='update-category'),
]
