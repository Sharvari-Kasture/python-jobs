# serializers.py
from rest_framework import serializers
from .models import Car, Maker

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class MakerSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = Maker
        fields = '__all__'

class MakerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = ('name', 'number_of_cars')

class CarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('maker', 'car_name', 'hpp', 'launch_date', 'mileage')