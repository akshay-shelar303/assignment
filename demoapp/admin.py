from django.contrib import admin
from .models import Customer, Policy


class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "age", "profession"]


admin.site.register(Customer, CustomerModelAdmin)


class PolicyModelAdmin(admin.ModelAdmin):
    list_display = ["policy_name", "period"]


admin.site.register(Policy, PolicyModelAdmin)