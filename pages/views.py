from django.shortcuts import render

# email
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    to_rotate_styles = [
        "Explore",
        "Create",
        "inspire or get inspired",
    ]
    owner = "Hi! I'm OpenSpace, "
    
    
    context = {
        'to_rotate_styles': to_rotate_styles,
        'owner': owner,
    }
    return render(request, 'pages/about.html', context)

def service(request):
    return render(request, 'pages/service.html')



def contact_view(request):
    print("contact page with: " + request.method)
    if request.method == "POST":
        # send the message
        form = ContactForm(request.POST)

        if form.is_valid():
            print("Sending email")

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data["message"]

            full_message = f"This is an email from your portfolio page\First name: {first_name}\n Last Name: {last_name}\nEmail: {email}\Phone: {phone}\nMessage: {message}"

            send_mail(
                "Email from " + first_name,
                full_message,
                email,
                ['openSpaceDjango@gmaill.com']
            )

            print("Email sent")

            # send the user to thank you page

        else:
            print("Invalid data on the form")
    else:
        # display page
        form = ContactForm()

    return render(request, "pages/contact.html", {"form": form})