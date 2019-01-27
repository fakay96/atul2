from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import MailBox,Inboxs
class Userss(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('email','username')
        #query=User.objects.get().values(fields)
class mailsserializer(serializers.ModelSerializer):
    class Meta:
        model=MailBox
        fields=('sender','recepient','message','cc',"subject","attachment")
class inboxserializer(serializers.ModelSerializer):
    class Metas:
        model=Inboxs
        fields=('sender','message','cc','attachment')
