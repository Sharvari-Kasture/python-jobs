from django.urls import path
from . import views

urlpatterns = [
    # Other app URLs
    path('login/', views.CustomLoginView.as_view(), name='custom_login'),
    path('logout/', views.CustomLogoutView.as_view(), name='custom_logout'),
    path('my-first-function/', views.my_first_function_view, name='my_first_function'),
    path('test/', views.test_view, name='test_route'),
    path('list/<str:suffix_string>/', views.car_list, name='car_list'),
    path('create/', views.create_maker, name='create_maker'),
    path('mlist/', views.maker_list, name='maker_list'),
]

