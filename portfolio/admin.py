from django.contrib import admin
from portfolio.models import *

# Register your models here.
class MessageAdminView(admin.ModelAdmin):
    list_display = ['id','name','email','msg']

admin.site.register(MessageInfo,MessageAdminView)

