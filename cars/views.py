from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from cars.models import Car
from django.utils import timezone
from django.http import HttpResponse

class CustomLoginView(LoginView):
    template_name = 'cars/login.html'
    success_url = reverse_lazy('home')  # Redirect to the 'home' page upon successful login
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_variable'] = 'This is a custom variable'
        return context

class CustomLogoutView(LogoutView):
    template_name = 'cars/logout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_variable'] = 'This is a custom variable'
        return context

def my_first_function_view(request):
    return HttpResponse("My First Function !@#")

def test_view(request):
    info = "This is the information returned from the test view."
    return HttpResponse(info)


def car_list(request, suffix_string):
    # Retrieve a list of cars with names starting with 'F'
    cars = Car.objects.filter(car_name__startswith='F')

    # Append the suffix_string to car names
    for car in cars:
        car.car_name += suffix_string

    # Pass the list of modified cars to the template
    context = {
        'cars': cars
    }
    print(f"Number of Cars: {len(cars)}")

    return render(request, 'cars/car_list.html', context)





