from django.shortcuts import render
from .models import *
from urllib import request
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .api import mailsserializer,inboxserializer,outboxserializer
from rest_framework.response import Response
from send2trash import send2trash
from rest_framework.views import APIView
class inbox(APIView):
    def get(self,request):
        user=request.user

        qwes=User.objects.get(username=user).email
        mailbox=MailBox.objects.all().filter(recepient=email).values('sender ','message','subject','cc')
        inbox=Inbox(mailbox)
        inbox.save()
        inn=Inboxs.object.all()
        serializer=inboxserializer(inn,many=True)
        hmtl="in.html"
        return Response({serializer.data})



def home(request):
    temp="email.html"
    return render(request,temp )


def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('recepient', '')
    user=request.user
    qwes=User.objects.get(username=user).email
    print(qwes)
    if subject and message and qwes:
        try:
            mail=MailBox(subject=subject,message=message,recepient=from_email,sender=qwes)
            mal=Outbox(subject=subject,message=message,recepient=from_email,sender=qwes)
            mal.save()
            mail.save()

        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('send_email')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
 
class Maills(APIView):
    def get(self,request):
        mail=MailBox.objects.all()
        serializer=mailsserializer(mail,many=True)

        return Response(serializer.data)



class Outbox(APIView):
    class Maills(APIView):
          def get(self,request):
                user=request.user

                qwes=User.objects.get(username=user).email
                mailbox=Outbox.objects.all().filter(recepient=email).values('recepient ','message','subject','cc','attachements')    
                serializer=outboxserializer(mailbox,many=True)

                return Response(serializer.data)



def emailthread():
    mail=[]
    if request.method =='GET':#recepent,mail subject,mail body
        query=mail.objects.all()
        mail.push(query)
        ui=mail.pop()
        return JsonResponse({ui.data})





def trashcan(request):
    Trashbutton=request.POST.get("Delete")
    emaildetails=request.POST.get("message")

    if Trashbutton:
        Trash=MailCompose.objects.get().filter(message=emaildetails) 
        fork=Trash.save(Trash)
        Trash.delete()
        sent2trash(delete)

class trash(APIView):
    def trashcan(request):
        user=request.user

        qwes=User.objects.get(username=user).email
        mailbox=Outbox.objects.all().filter(recepient=email).values('attachment','sender ','message','subject','cc')
        serialize=trashseralizer(mailbox,many=True)
        return Respose({serialize.data})
        
    




