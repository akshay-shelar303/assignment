from django.db import models
from .policy_choices import government_policies


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    profession = models.CharField(max_length=100)
    


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Policy(models.Model):
    policy_name = models.CharField(max_length=300, choices=government_policies)
    period = models.IntegerField()
    customer = models.ManyToManyField(Customer)


    def __str__(self):
        return self.policy_name
    