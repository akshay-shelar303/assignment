from django.urls import path

from .views import Notify, UpdateNotify


urlpatterns = [
    path("notify/", Notify.as_view(), name="notify"),
    path("updatenotify/<int:pk>/", UpdateNotify.as_view(), name="update"),
]
