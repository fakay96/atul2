from __future__ import print_function
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

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def home():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

if __name__ == '__main__':
    main()

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
        
    




