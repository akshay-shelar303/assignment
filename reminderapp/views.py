from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Notification
from .serializers import NotificationSerializer


class Notify(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def get(self, request):
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        notification = Notification.objects.get(id=self.id)
        serializer = NotificationSerializer(
            notification, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateNotify(APIView):
    def get(self, request, pk):
        try:
            notification = Notification.objects.get(id=pk)
        except Exception as e:
            return Response({"msg": f"Record with id={pk} does not exist"})

        serializer = NotificationSerializer(notification)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            notification = Notification.objects.get(id=pk)
        except:
            return Response({"msg": f"Record with id={pk} does not exist"})

        serializer = NotificationSerializer(
            notification, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            notification = Notification.objects.get(id=pk)
        except:
            return Response({"msg": f"Record with id={pk} does not exist"})

        notification.delete()
        return Response(
            {"msg": "Record deleted successfully", "status": status.HTTP_200_OK}
        )
