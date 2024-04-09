from django.urls import path
from .views import ProductBillingListCreateAPIView, ProductBillingRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', ProductBillingListCreateAPIView.as_view(), name='product-billing-list-create'),
    path('<int:pk>/', ProductBillingRetrieveUpdateDestroyAPIView.as_view(), name='product-billing-detail'),
]