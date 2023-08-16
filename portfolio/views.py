from django.http import HttpResponse
from django.shortcuts import redirect, render
from portfolio.models import *

# Code to add the frontend messages in the database
def dataHandler(request):
    if request.method == 'POST':
        name = request.POST['fullName']
        email = request.POST['emailid']
        msg = request.POST['message']
        MessageInfo.objects.create(name=name,email=email,msg=msg)
    services=ServiceInfo.objects.all()
    projects=ProjectInfo.objects.all()
    testimonials=TestimonialInfo.objects.all()
    blogs=BlogInfo.objects.all()
    context={
        'services': services,
        'projects': projects,
        'testimonials': testimonials,
        'blogs': blogs,
    }
    return render(request,'portfolio/index.html',context)
       
