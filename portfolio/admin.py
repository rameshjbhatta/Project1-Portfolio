from django.contrib import admin
from portfolio.models import *

# Register your models here.
class MessageAdminView(admin.ModelAdmin):
    list_display = ['id','name','email','msg']

class ServiceAdminView(admin.ModelAdmin):
    list_display = ['id','service_image','service_title','service_sub_title']  

class ProjectAdminView(admin.ModelAdmin):
    list_display = ['id','project_category','project_name','project_image']

class TestimonialAdminView(admin.ModelAdmin):
    list_display = ['id','client_name','client_opinion','client_image']

class BlogAdminView(admin.ModelAdmin):
    list_display = ['id','blog_author','blog_title','blog_content','blog_image']    

admin.site.register(MessageInfo,MessageAdminView)
admin.site.register(ServiceInfo,ServiceAdminView)
admin.site.register(ProjectInfo,ProjectAdminView)
admin.site.register(TestimonialInfo,TestimonialAdminView)
admin.site.register(BlogInfo,BlogAdminView)

