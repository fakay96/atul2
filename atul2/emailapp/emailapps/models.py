from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
 
LIMIT_FOR_MAIL = 1000000000
LIMIT_FOR_CC = 10000
LIMIT_FOR_TO = 10000
LIMIT_FOR_ATTACHMENTS = 100


class MailCompose(models.Model):
    
    #userf=sentmails.__get__(userf)
    global LIMIT_FOR_MAIL
    global LIMIT
    message=models.TextField(default="",max_length=LIMIT_FOR_MAIL)   
    # editable=False, beacuse once a user logged in it shouldnt get updated.
    sender=models.EmailField(default=User,editable=False)
    recepient=models.CharField(default="",max_length=100)
    a=[]
    lenght=len(a)
    cc=models.CharField(default=a,max_length=LIMIT_FOR_CC)
    def __str__(self):
            return self.message[:50] + '...'
       
class Drafts(MailCompose):
     
    mail=MailCompose
   

#its from the argument Mailcompose ....


#drafts??
#...i think it should have the same structure as the mail??......cant we inheritance ,as a foreinGS key?
#i thin its possible its a public class??
#lets try with inheritance...if doesnot work we can always implement seperate class.
#ok .im not good with oop tho can you please show me  ithink its extends fro ja....vsaure I can guide you...
# auto complete of the email address from DB is inbuilt feature of django ?
#no ,we creating it
#what we can do is  choices=("fak":faka       
# the models not migrting.........
#    
# y(#6got it...))
class Outbox(MailCompose):
    mail=MailCompose

class ReplyTo(MPTTModel):
    message = models.ForeignKey(MailCompose, related_name='comments',on_delete=models.CASCADE)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children',db_index=True, on_delete=models.CASCADE)
    reply = models.CharField(max_length=500, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
        # approved = models.BooleanField(default=False)
    class MPTTMeta:
            order_insertion_by = ['date_added']

            def __str__(self):
               return self.user_reply[:20]
class Trash(MailCompose):
    mail=MailCompose






    