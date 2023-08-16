from django.shortcuts import  render
from portfolio.models import *
from django.contrib import messages

from django.http import HttpResponse
import mimetypes

def download_file(request):
    # Fill these variables with real values
    fl_path = 'portfolio/static/files/CV Ramesh Bhatta.pdf'
    filename = 'CV Ramesh Bhatta.pdf'

    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response



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
       
