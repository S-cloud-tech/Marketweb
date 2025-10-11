from django.shortcuts import render
from .models import *
from blog.models import Post
from item.models import Item

def home(request):

    
    post = Post.objects.all()
    service = Service.objects.all()
    testimonial = Testimonial.objects.all()

    context = {
        "post": post,
        "service": service,
        "testimonial": testimonial
    }


    return render(request, "home.html", context)

