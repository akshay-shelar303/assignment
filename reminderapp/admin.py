from django.contrib import admin

from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ["date", "time", "message"]


admin.site.register(Notification, NotificationAdmin)
