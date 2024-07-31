from django.urls import path
from .views import CustomerView

urlpatterns = [
     path('details/', CustomerView.as_view(), name='customer-list-create'),
]

