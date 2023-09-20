from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from cars.models import Car, Maker
from django.utils import timezone
from django.http import HttpResponse
from .forms import MakerForm

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
    # Retrieve a list of all cars
    cars = Car.objects.all()
    current_date = timezone.now()
    cars = Car.objects.filter(launch_date__gt=current_date)

    # Filter cars with names starting with 'F'
    cars_with_f = [car for car in cars if car.car_name.startswith('F')]

    # Append the suffix_string to car names
    for car in cars_with_f:
        car.car_name += suffix_string

    # Pass the list of modified cars to the template
    context = {
        'cars': cars_with_f
    }

    return render(request, 'cars/car_list.html', context)

def maker_list(request):
    makers = Maker.objects.all()
    return render(request, 'cars/maker_list.html', {'makers': makers})


def create_maker(request):
    if request.method == 'POST':
        form = MakerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maker_list')  # Redirect to the list view after creating a Maker
    else:
        form = MakerForm()

    return render(request, 'cars/maker_form.html', {'form': form})






