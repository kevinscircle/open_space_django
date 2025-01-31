from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView
from users.models import Profile
from .models import Product
from.forms import UpdateProfileForm
from django.urls import reverse

# Create your views here.
# def index(request):
#     return HttpResponse("Welcome to index")


# Profile 


class ProfileView(ListView):
    template_name = 'services/profile.html'
    model = Profile

class ProfileUpdateView(UpdateView):
    template_name ='services/profile_update.html'
    model = Profile
    form_class = UpdateProfileForm

    def get_success_url(self):
        return reverse('services:profile')




# products 

class ProductListView(ListView):
    template_name = 'services/products.html'
    model = Product