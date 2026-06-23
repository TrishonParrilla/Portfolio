from django.shortcuts import render

# Create your views here.
def about_me_view(request):
    return render(request, 'pages/about.html')

def experience_view(request):
    return render(request, 'pages/experience.html')

def contact_view(request):
    return render(request, 'pages/contact.html')

def projects_view(request):
    return render(request, 'pages/projects.html')
