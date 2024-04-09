from .models import Product
from rest_framework import serializers
from shopping_mall.users.models import User

class ProductSerializer(serializers.ModelSerializer):
    added_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'added_by']