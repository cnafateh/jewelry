from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['phone', 'address', 'city', 'country', 'zipcode']
        model = Customer
        