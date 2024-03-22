from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet



class UserDetails(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
