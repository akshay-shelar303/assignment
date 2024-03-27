from rest_framework.viewsets import ModelViewSet
from .models import Customer, Policy
from .serializers import CustomerSerializer, PolicySerializer


class CutomerModelViewset(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class PolicyModelViewset(ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer


