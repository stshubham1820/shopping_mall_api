from rest_framework import status,generics
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from shopping_mall.users.models import User
from django.db import IntegrityError
from shopping_mall.product_billing.serializers import InvoiceSerializer
from .serializers import UserSerializer,UserRegisterSerializer


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "pk"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=True,methods=['post'], name='invoice')
    def generate_invoice(self, request,pk=None):
        try :
            print(request.data)
            
            invoice_data = InvoiceSerializer(data=request.data)
            if invoice_data.is_valid():
                invoice_data.save()
                res_status = status.HTTP_200_OK
                res_data = invoice_data.data
            else :
                res_status = status.HTTP_400_BAD_REQUEST
                res_data = invoice_data.errors 
        except Exception as err:
            res_status = status.HTTP_500_INTERNAL_SERVER_ERROR
            res_data = {'error':str(err)}
        finally:
            return Response(status=res_status, data=res_data)


class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e:
            return Response({'error': 'User with the following e-mail already exist'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'An error occurred during registration.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)