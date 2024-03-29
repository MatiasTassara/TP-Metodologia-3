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
    name = models.CharField(max_length=50, default="")
    code = models.IntegerField()
    total = models.IntegerField()

class RentDate(models.Model):
    date = models.DateField()
    RealState = models.ForeignKey(RealState, null=False, on_delete=models.SET('null'), related_name='rents')
    reservation = models.ForeignKey(Reservation, null=True, blank=True, default=None, on_delete=models.SET('null'), related_name='rents')

    def __str__(self):
        return datetime.strftime(self.date, '%d/%m/%Y') +  str(self.RealState) + str(self.id)
