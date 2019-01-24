from django.shortcuts import render
from .models import *
from urllib import request
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .api import mailsserializer
from django_handlers import Handler
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
#@handler.get('mails')
 

# message :"helllloooooo"
# sender :"fakay96@gmail.com"
# recepient:"ceceee@gmail.com"
#         
# message :"helllloooooo"
# sender :"fakay96@gmail.com"
# recepient:"ceceee@gmail.com"
#         
# message :"helllloooooo"
# sender :"fakay96@gmail.com"
# recepient:"ceceee@gmail.com"
#         
  

#require json tags coming from the ui to 
# 
# 
#     

def send_multiple_emails():
    def send_mail():
        pass
    pass

    
#if json tags contains "cc"
# we would call the function send multiple 
# we can implement sender function with and without cc..
#if cc is empty that loop will execute zero times, if cc has some emails then it will execute that many times. ?
#else call the function send mail?..ok.

def threadsToSendMail():
    mail=[]
    if request.method =='GET':#recepent,mail subject,mail body
        query=mail.objects.all()
        mail.push(query)
        ui=mail.pop()
        return JsonResponse({ui.data})
#a=groupby(ui.data.recepient) so therefore all reciepients are treated as one on the ui and we can have threadlike structure
#sry,...i didnt get u..
#okay im saying we will use the ui.data.recepient as a basis fro  our thread, since the messages sent to .....


# threads may be some key word...so cant we rename it to threadsToSendMail.kkkkk
#I am reading from re....
#  2: trash box
#3: in adddtion to auto complete for to list(we have to validate the to/cc are correct email as per the DB)
#yeah





#my sister is stranded somewherre trying to send her money but i myself don have enough :
# I will release payment for this adhoc work ASAP...dont worry..soon u will have enoug
#loooool :). ok...
#:)Back to work...k


#letspick it one by one so as to not go out of scope. i will complete the  things we discussed today??
#sounds good.k
#can we start now??
#or you busy
#we can start now


