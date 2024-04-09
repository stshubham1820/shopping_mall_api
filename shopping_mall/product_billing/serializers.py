from rest_framework import serializers
from .models import ProductBilling,Invoice
from shopping_mall.product.serializers import ProductSerializer

class ProductListSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True,read_only=True)
    class Meta:
        model = ProductBilling
        fields = '__all__'

class ProductBillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBilling
        fields = ['id', 'product', 'quantity', 'discount', 'final_price']
        read_only_fields = ['final_price']

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Quantity must be at least 1.")
        return value

    def validate_discount(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("Discount must be between 0 and 100.")
        return value

def calculate_total_amount(data):
        total_amount = sum(product.final_price for product in data.products.all())
        return total_amount

class InvoiceSerializer(serializers.ModelSerializer):
    product_details = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Invoice
        fields = '__all__'
        read_only_fields = ['total_amount']

    def create(self, validated_data):
        data = super().create(validated_data)
        data.total_amount = calculate_total_amount(data)
        data.save()
        return data
    def get_product_details(self,obj):
        _list = []
        data = obj.products.all()
        if len(data) != 0 :
            for i in data:
                _dict = {}
                _dict['id'] = i.id
                _dict['product'] = {
                    'name' : i.product.name,
                    'description' : i.product.description,
                    'price' : i.product.price

                }
                _dict['quantity'] = i.quantity
                _dict['discount'] = i.discount
                _dict['final_price'] = i.final_price
                _list.append(_dict)
        return _list