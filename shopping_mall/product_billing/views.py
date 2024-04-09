from rest_framework import generics
from .models import ProductBilling
from .serializers import ProductBillingSerializer

class ProductBillingListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductBilling.objects.all()
    serializer_class = ProductBillingSerializer

class ProductBillingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductBilling.objects.all()
    serializer_class = ProductBillingSerializer