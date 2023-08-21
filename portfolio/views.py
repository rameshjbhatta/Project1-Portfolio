from django.shortcuts import  render
from portfolio.models import *
from django.contrib import messages

from django.http import HttpResponse
import mimetypes

def downloadFile(request):
    file_path = 'portfolio/static/files/CV Ramesh Bhatta.pdf'
    filename = 'CV Ramesh Bhatta.pdf'

    file = open(file_path, 'rb') #open file in read mode
    mime_type, _ = mimetypes.guess_type(file_path)  # find  9file0 media type 
    response = HttpResponse(file, content_type=mime_type) # creates an HttpResponse object, which will be used to respond to the client's request.
    response['Content-Disposition'] = "attachment; filename=%s" % filename #sets the Content-Disposition HTTP header in the response.
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
       
