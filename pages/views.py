from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def about_me_view(request):
    return render(request, 'pages/about.html')

def experience_view(request):
    return render(request, 'pages/experience.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            #Build the full email content

            message_body = (
                f'you have a new email from your portfolio contact form\n\n'
                f'Name: {name}\n'
                f'Email: {email}\n'
                f'Message: {message}\n'
            )
            try:
                #send email using django's send_mail function
                send_mail(
                    "Email from Portfolio Contact Form", #subject
                    message_body, #message
                    email, #from email
                    ['trishonp1@gmail.com']
                )
                form = ContactForm()  # reset the form after successful submission
                return render(request, 'pages/contact.html', {'form': form})
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Form is not valid")
            return render(request, 'pages/contact.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'pages/contact.html', {'form': form})

    form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})



