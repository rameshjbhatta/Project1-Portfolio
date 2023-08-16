from django.shortcuts import  render
from portfolio.models import *
from django.contrib import messages


# Code to add the frontend messages in the database
def dataHandler(request):
    if request.method == 'POST':
        name = request.POST['fullName']
        email = request.POST['emailid']
        msg = request.POST['message']
        try:
            MessageInfo.objects.create(name=name, email=email, msg=msg)
            messages.success(request, 'Message sent successfully!')
        except:
            messages.error(request, 'Error sending message')

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
       
