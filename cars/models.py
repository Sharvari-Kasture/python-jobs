from django.db import models
from django.utils import timezone


class Maker(models.Model):
    name = models.CharField(max_length=255)
    number_of_cars = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=255)
    hpp = models.IntegerField()
    launch_date = models.DateField()

    def __str__(self):
        return self.car_name

