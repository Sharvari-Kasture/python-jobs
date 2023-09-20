import random
from django.core.management.base import BaseCommand
from faker import Faker
from cars.models import Car, Maker

fake = Faker()  # Initialize the Faker instance

class Command(BaseCommand):
    help = 'Populate the database with dummy data for the Car model'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating dummy data for the Car model...'))

        try:
            # Create some dummy Maker records
            for _ in range(10):
                maker_name = fake.company()  # Generate fake company names
                Maker.objects.create(name=maker_name)

            self.stdout.write(self.style.SUCCESS('Successfully created dummy Maker data.'))

            # Create 100 unique records with random data
            for _ in range(100):
                maker = random.choice(Maker.objects.all())
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
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
        finally:
            self.stdout.write(self.style.SUCCESS('Process completed.'))
