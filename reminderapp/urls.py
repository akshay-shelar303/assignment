from django.urls import path
from .views import notifyView, Notify, UpdateNotify


urlpatterns = [
    path("reminder/", notifyView, name="reminder"),
    path("notify/", Notify.as_view(), name="notify"),
    path("updatenotify/<int:pk>/", UpdateNotify.as_view(), name="update"),
]
