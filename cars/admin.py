from django.contrib import admin
from .models import Car, Maker

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'maker', 'hpp', 'launch_date')
    list_filter = ('maker', 'launch_date')
    search_fields = ('car_name', 'maker__name')
    list_per_page = 25

@admin.register(Maker)
class MakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_cars', 'number_of_cars', 'updated_at')
    search_fields = ('name', 'number_of_cars')

    def display_cars(self, obj):
        # Get the cars associated with the maker
        cars = obj.car_set.all()
        car_count = cars.count()

        if car_count < 2:
            # Display car Name and horsepower
            return ', '.join([f"{car.car_name} ({car.hpp} HP)" for car in cars])
        elif 2 <= car_count <= 5:
            # Display only car names
            return ', '.join([car.car_name for car in cars])
        else:
            # Display all cars in a dropdown
            return 'All Cars (Dropdown)'

    display_cars.short_description = 'Cars Made'
