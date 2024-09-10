from rest_framework.viewsets import ModelViewSet
from .models import Customer, Policy
from .serializers import CustomerSerializer, PolicySerializer, ViewPolicySerializer


class CutomerModelViewset(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class PolicyModelViewset(ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    serializer_action_classes = {'list': ViewPolicySerializer, 'retrieve': ViewPolicySerializer}

    def get_serializer_class(self) :
        try:
            return self.serializer_action_classes[self.action]
        
        except (KeyError, AttributeError):
            return super().get_serializer_class()



