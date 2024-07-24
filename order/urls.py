from django.urls import path
from .views import OrderApi, UserOrderApi

urlpatterns = [
    path("", OrderApi.as_view()),
    path("user_orders/", UserOrderApi.as_view()),
]


