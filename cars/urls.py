from django.urls import path
from . import views

urlpatterns = [
    # Other app URLs
    path('login/', views.CustomLoginView.as_view(), name='custom_login'),
    path('logout/', views.CustomLogoutView.as_view(), name='custom_logout'),
    path('my-first-function/', views.my_first_function_view, name='my_first_function'),
    path('test/', views.test_view, name='test_route'),
    path('list/', views.car_list, name='car_list'),
]

