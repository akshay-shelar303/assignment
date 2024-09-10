from rest_framework.serializers import ModelSerializer
from .models import Customer, Policy


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class PolicySerializer(ModelSerializer):
    class Meta:
        model = Policy
        fields = "__all__"


class ViewPolicySerializer(ModelSerializer):
    class Meta:
        model = Policy
        fields = "__all__"
        depth = 1