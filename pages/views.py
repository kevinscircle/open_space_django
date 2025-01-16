from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    to_rotate_styles = [
    "Explore",
    "Create",
    "inspire or get inspired",
    ]

    owner= "Kevin"
    return render(request, 'pages/about.html', {"to_rotate_styles":to_rotate_styles, "owner":owner})

def service(request):
    return render(request, 'pages/service.html')

def contact(request):
    return render(request, 'pages/contact.html')




