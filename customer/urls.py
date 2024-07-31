from django.urls import path
from .views import CustomerView

urlpatterns = [
    # path('', CustomerListCreateView.as_view())
     path('customers/', CustomerView.as_view(), name='customer-list-create'),
]

