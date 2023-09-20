from django.db import models

class Maker(models.Model):
    name = models.CharField(max_length=255)
    number_of_cars = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Car(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=255)
    hpp = models.IntegerField()
    launch_date = models.DateField()

    def __str__(self):
        return self.car_name

