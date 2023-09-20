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
    list_display = ('name', 'number_of_cars', 'updated_at')
    search_fields = ('name', 'number_of_cars')

