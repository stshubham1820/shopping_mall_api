from rest_framework import serializers

from shopping_mall.users.models import User
from django.contrib.auth.hashers import check_password,make_password

class UserSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        fields = ["name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "pk"},
        }


class UserRegisterSerializer(serializers.ModelSerializer[User]):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["name", "email","password"]

    def create(self, validated_data):
        if validated_data.get('password'):
            validated_data['password'] = make_password(validated_data.pop('password'))
        data = super().create(validated_data)
        return data