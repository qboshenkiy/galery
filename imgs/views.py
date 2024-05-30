from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import ImageModel
# Create your views here.
def index(requsets):
    image = ImageModel.objects.all()
    context ={
        'image': image
    }
    return render(requsets, 'index.html', context)

@require_POST
def send_feedback_email(request):
    ad = request.POST.get('ad', '')
    email = request.POST.get('email', '')
    msg = request.POST.get('msg', '')

    subject = 'Feedback from website'
    from_email = ''
    to_email = ''
    body = f'Message: {msg}\nAd: {ad}\nEmail: {email}'


    send_mail(subject, body, from_email, [to_email])

    return redirect('home')