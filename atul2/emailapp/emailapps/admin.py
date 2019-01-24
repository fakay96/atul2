from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(MailCompose)
admin.site.register(Drafts)
admin.site.register(Outbox)
admin.site.register(ReplyTo)