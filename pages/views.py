from django.shortcuts import render
from .forms import ContactForm
# Create your views here.
def about_me_view(request):
    return render(request, 'pages/about.html')

def experience_view(request):
    return render(request, 'pages/experience.html')

def contact_view(request):
    form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})



