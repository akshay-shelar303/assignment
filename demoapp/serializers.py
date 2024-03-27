from rest_framework.serializers import ModelSerializer
from .models import Customer, Policy



class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class PolicySerializer(ModelSerializer):
    customer = CustomerSerializer(read_only=True, many=True)
    class Meta:
        model = Policy
        fields = "__all__"