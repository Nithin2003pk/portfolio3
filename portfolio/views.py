from django.shortcuts import render
from django.core.mail import send_mail
from .models import Project, Contact

def home(request):
    projects = Project.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to database
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Send email
        send_mail(
            subject=f"New message from {name}",
            message=f"Email: {email}\n\nMessage:\n{message}",
            from_email='nithinpk136@gmail.com',
            recipient_list=['nithinpk136@gmail.com'],
            fail_silently=False,
        )

    return render(request, "index.html", {'projects': projects})

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'nithinpk136@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password_here'