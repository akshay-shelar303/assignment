from django.urls import path
from .views import notifyView


urlpatterns = [
    path("reminder/", notifyView, name='reminder')
]
