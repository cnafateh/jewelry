from rest_framework import generics, permissions, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer
from .models import Order
from rest_framework import generics, permissions
from customer.models import Customer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        customer = Customer.objects.get(user=self.request.user)
        serializer.save(user=customer)

    def get_queryset(self):
        customer = Customer.objects.get(user=self.request.user)
        return self.queryset.filter(user=customer)



# class OrderApi(APIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     def post(self, request):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=200)
#         else:
#             return Response({"errors": serializer.errors}, status=400)