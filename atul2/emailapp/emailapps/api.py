from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from emailapps.models import MailCompose
class Userss(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('email','username')
        #query=User.objects.get().values(fields)
class mailsserializer(serializers.ModelSerializer):
    class Meta:
        model=MailCompose
        fields=('sender','recepient','message','cc')