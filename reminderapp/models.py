from django.db import models


class Notification(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()

    def __str__(self):
        return self.message
