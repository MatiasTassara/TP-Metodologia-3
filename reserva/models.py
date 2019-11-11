from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)
    province = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RealState(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    capacity = models.IntegerField()
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(User, null=False, on_delete=models.SET('null'))
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    date = models.DateTimeField()
    code = models.IntegerField()
    total = models.IntegerField()
    RealState = models.ForeignKey(RealState, null=False, on_delete=models.SET('null'))

    def __str__(self):
        return datetime.strftime(self.date, '%d/%m/%Y')


class RentDate(models.Model):
    date = models.DateTimeField()
    RealState = models.ForeignKey(RealState, null=False, on_delete=models.SET('null'))
    reservation = models.ForeignKey(Reservation, null=False, on_delete=models.SET('null'))

    def __str__(self):
        return self.date