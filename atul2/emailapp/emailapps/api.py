from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import *
class Userss(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('email','username')
        query=User.objects.get().values(fields)
class mailserializer(serializers.ModelSerializer):
    class Meta:
        model= mail
        fields=('sender','receipient','cc','message')
        

