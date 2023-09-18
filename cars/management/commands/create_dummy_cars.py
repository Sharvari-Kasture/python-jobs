import random
from django.core.management.base import BaseCommand
from faker import Faker
from cars.models import Car, Maker

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the Car model with dummy data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating dummy Car data...'))

        # Check if there are any Maker objects
        if not Maker.objects.exists():
            #self.stdout.write(self.style.WARNING('No Maker objects found. Cannot create dummy Car data.'))
            return

        # Retrieve existing Maker objects
        makers = Maker.objects.all()

        # Create 100 unique Car instances with random data
        for _ in range(100):
            maker = random.choice(makers)
            car_name = fake.unique.first_name()  # Ensure car names are unique
            hpp = random.randint(100, 500)
            launch_date = fake.date_between(start_date='-30y', end_date='today')

            Car.objects.create(
                maker=maker,
                car_name=car_name,
                hpp=hpp,
                launch_date=launch_date
            )

        self.stdout.write(self.style.SUCCESS('Successfully created dummy Car data.'))
