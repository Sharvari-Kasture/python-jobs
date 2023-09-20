from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from .sitemaps import StaticViewSitemap
from .views import HomeView, ApplyView
from cars.views import CustomLoginView, CarListView
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

   # path('login/', lambda request: redirect('/accounts/login/')),  # Redirect /login/ to /accounts/login/
   # path('logout/', lambda request: redirect('accounts/logout/')), # Redirect /login/ to /accounts/logout/
]

# Sitemap
sitemaps = {
    'static': StaticViewSitemap
}

urlpatterns += [
    path('sitemap/', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap_xml'),
]

urlpatterns += [
    path('', HomeView.as_view(), name='home'),
    path('apply/', ApplyView.as_view(), name='apply'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('clist/', CarListView.as_view(), name='car-list'),
    path('cars/', include('cars.urls')),  # Include 'cars' app URLs
    path('maker/', include('cars.urls')), 
]
