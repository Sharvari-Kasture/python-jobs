from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from xcv_seo.mixin import SEOMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from cars.models import Car, Maker
from django.utils import timezone
from django.http import HttpResponse
from .forms import MakerForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView

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
    
@login_required
class HomeView(SEOMixin, TemplateView):
    template_name = 'home.html'
    extra_context = {
        "roles": [
            {
                "name": "Senior Developer"
            },
            {
                "name": "Developer"
            },
            {
                "name": "Intern"
            },
            {
                "name": "Summer Intern"
            }
        ],
        "responsibilities": [
            {
                "name": "Develop applications"
            },
            {
                "name": "Write tests"
            },
            {
                "name": "Write documentation"
            },
            {
                "name": "Deploy applications"
            }
        ],
        "requirements": [
            {
                "name": "Minimum",
                "items": [
                    "Excellent communication skills",
                    "Strong analytical skills",
                    "Obsessed with details",
                    "Programming experience",
                    "Experience with one or more general-purpose languages",
                    "Expertise in Python 3.7+"
                ]
            },
            {
                "name": "Preferred",
                "items": [
                    "Linux",
                    "Shell scripting",
                    "Git (GitHub and/or Bitbucket)",
                    "Django",
                    "Flask",
                    "JavaScript",
                    "HTML5/CSS",
                    "Bootstrap",
                ]
            },
            {
                "name": "Extra",
                "items": [
                    "Numpy",
                    "Pandas",
                    "D3",
                    "Solved Project Euler (<a href='https://projecteuler.net/'>projecteuler.net</a>) problems",
                ]
            }
        ]
    }

class ApplyView(SEOMixin, TemplateView):
    template_name = 'apply.html'

class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    context_object_name = 'cars'
    paginate_by = 25  # Set the number of cars to display per page
    
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
            maker = form.save(commit=False)
            maker.updated_at = timezone.now()  # Set the updated_at field to the current timestamp
            maker.save()
            return HttpResponseRedirect('https://www.google.com/')  # Redirect to google.com
    else:
        form = MakerForm()
    
    return render(request, 'cars/maker_form.html', {'form': form})






