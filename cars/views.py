from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from xcv_seo.mixin import SEOMixin

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
