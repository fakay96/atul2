from django.shortcuts import render
from .models import *
from urllib import request
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
def sentmails(request):
    mail=[]
    maillist=mail.objects.get().values("mail","sender","recepient","cc")
    mail.append(maillist)
    ui=mail.pop()
    userf=request.User.email
    return userf