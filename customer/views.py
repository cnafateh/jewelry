from rest_framework import generics, permissions, status
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# class CustomerListCreateView(APIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request):
#         serializer = CustomerSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=200)
#         else:
#             return Response({"errors": serializer.errors}, status=400)
# **************************************************************************************
# class CustomerListCreateView(generics.ListCreateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class CustomerRetrieveUpdateView(generics.RetrieveUpdateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#     permission_classes = [permissions.IsAuthenticated]
# **************************************************************************************
class CustomerView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        customers = Customer.objects.filter(user=request.user)
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        # پیدا کردن مشتری مرتبط با کاربر جاری
        customer = get_object_or_404(Customer, user=request.user)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)