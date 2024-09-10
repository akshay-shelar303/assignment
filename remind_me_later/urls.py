
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from AccountsApp.views import UserDetails
from demoapp.views import CutomerModelViewset, PolicyModelViewset

router = DefaultRouter()
router.register('accounts', UserDetails, basename='accounts')

router.register('customer', CutomerModelViewset, basename="customer")

router.register('policy', PolicyModelViewset, basename="policy")


urlpatterns = [
    path("admin/", admin.site.urls), 
    path("", include("reminderapp.urls")),
    path('api/', include(router.urls)),
    path('user/', include("AccountsApp.urls"))
    ]
