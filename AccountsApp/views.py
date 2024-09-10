from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view



class UserDetails(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(["GET", "POST"])
def user_registration(request):
    serializer = UserSerializer(request.data)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        user = User.objects.create_user(username=username, password=password, email=email)
        print(user)
        if user.is_authenticated():
            user.save()
            print(user)
            return Response("data collected")


    return Response("user created")
