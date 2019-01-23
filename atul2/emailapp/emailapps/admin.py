from django.contrib import admin
from .models import *

# Register your models here.
class mailsRegister(admin.ModelAdmin):
    class meta:
        model=mail
admin.site.register(mail,mailsRegister )