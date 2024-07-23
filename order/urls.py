from django.urls import path
from .views import OrderApi

urlpatterns = [
    path("", OrderApi.as_view()),
]


