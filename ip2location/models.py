from django.utils import timezone
from django.db import models




class History(models.Model):
    access = models.DateTimeField(default=timezone.now)
    ip = models.CharField(max_length=15)
    country_short = models.CharField(max_length=3)
    country_long = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    coordinates = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=15)
    timezone = models.CharField(max_length=15)

    def __str__(self):
        return self.ip
