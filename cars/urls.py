from django.urls import path
from . import views

urlpatterns = [
    # Other app URLs
    path('login/', views.CustomLoginView.as_view(), name='custom_login'),
    path('logout/', views.CustomLogoutView.as_view(), name='custom_logout'),
]

