from django.db import models
from django.utils import timezone
from django.db.models.signals import Signal, post_save
from django.dispatch import receiver

car_created = Signal(providing_args=["car_instance"])

class Maker(models.Model):
    name = models.CharField(max_length=255)
    number_of_cars = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=255, unique=True)
    hpp = models.PositiveIntegerField()
    launch_date = models.DateField()
    mileage = models.FloatField(null=True)


    def __str__(self):
        return self.car_name
    
car_created = Signal()

# Signal handler function
@receiver(car_created)
def update_maker_car_count(sender, car_instance, **kwargs):
    maker = car_instance.maker
    maker.number_of_cars += 1
    maker.save()

# Connect the signal handler to the post_save signal of Car model
post_save.connect(update_maker_car_count, sender=Car)


