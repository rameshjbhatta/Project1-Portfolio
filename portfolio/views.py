from django.http import HttpResponse
from django.shortcuts import redirect, render
from portfolio.models import *

# Code to add the frontend messages in the database
def messageHandler(request):
    if request.method == 'POST':
        name = request.POST['fullName']
        email = request.POST['emailid']
        msg = request.POST['message']
        MessageInfo.objects.create(name=name,email=email,msg=msg)
    messages = MessageInfo.objects.all()
    return render(request,'index.html',{'messages':messages})
       
def serviceHandler(request):
    services=ServiceInfo.objects.all()
    return render(request,'index.html',{'services':services})
