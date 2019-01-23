from django.db import models
from .views import sentmails
class mail(models.Model):
    #userf=sentmails.__get__(userf)
    message=models.TextField(default="",max_length=1000000000)         
    sender=models.EmailField(default=sentmails,editable=False)
    recepient=models.CharField(default="",max_length=100)
    a=[                                                                        ]
    lenght=len(a)
    cc=models.CharField(default=a,max_length=100000000)
        
       
class drafts(models.Model):

            mail=models.TextfieldField(default="",max_length="")
            sender=models.EmailField(default=sentmails,editable=False)
            recepient=models.CharField(default="",max_length=100)
            a=[]
            
            cc=models.CharField(default=a,max_length=10000)



class outbox(models.Model):
    mailes=models.ForeignKey(mail,on_delete=models.CASCADE)

class mailingadrress(models.Model):
    emailaddresses=models.ForeignKey(mail,on_delete=models.CASCADE)









    