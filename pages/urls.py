from django.urls import path
from .views import home, about, service, contact_view

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('service', service, name='service'),
    path('contact', contact_view, name='contact')
]