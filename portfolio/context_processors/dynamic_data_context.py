from portfolio.models import ServiceInfo, ProjectInfo, TestimonialInfo, BlogInfo

def dynamic_data_context(request):
    services = ServiceInfo.objects.all()
    projects = ProjectInfo.objects.all()
    testimonials = TestimonialInfo.objects.all()
    blogs = BlogInfo.objects.all()
    return {
        'services': services,
        'projects': projects,
        'testimonials': testimonials,
        'blogs': blogs,
    }
