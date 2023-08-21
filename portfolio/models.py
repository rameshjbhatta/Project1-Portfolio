from django.db import models

# Create your models here.
class MessageInfo(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=150)
    msg = models.TextField(max_length=350)
    
class ServiceInfo(models.Model):
       service_image = models.ImageField(upload_to='images/', null=True)
       service_title=models.CharField(max_length=250,default='title')
       service_sub_title=models.TextField(max_length=300,default='sub-title')

class ProjectInfo(models.Model):
       project_link=models.URLField(max_length=200,default=1)
       project_image = models.ImageField(upload_to='images/', null=True)
       project_category=models.CharField(max_length=250)
       project_name=models.CharField(max_length=250)       
       
class TestimonialInfo(models.Model):
       client_image = models.ImageField(upload_to='images/', null=True)
       client_opinion=models.TextField(max_length=400)
       client_name=models.CharField(max_length=250)         

class BlogInfo(models.Model):
       blog_author=models.CharField(max_length=100)
       blog_image = models.ImageField(upload_to='images/', null=True)
       blog_title=models.CharField(max_length=400)
       blog_content=models.TextField(max_length=600)     

class Like(models.Model):
    session_key = models.CharField(max_length=40, null=True, blank=True, default='guest_session')  # Store the session key or guest identifier
    blog = models.ForeignKey(BlogInfo, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)  

        