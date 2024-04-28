from django.shortcuts import render
from . import models


def index(request):
    categories = models.Category.objects.all()
    regions = models.Region.objects.all()
    posts = models.Post.objects.all()
    context = {
        'regions': regions,
        'categories': categories,
        'posts': posts
    }
    return render(request, 'front/index.html', context)


def single_post(request):
    categories = models.Category.objects.all()
    regions = models.Region.objects.all()
    posts = models.Post.objects.all()
    context = {
        'regions': regions,
        'categories': categories,
        'posts':posts
    }
    return render(request, 'front/single-post.html', context)



def contact(request):
    categories = models.Category.objects.all()
    regions = models.Region.objects.all()
    context = {
        'regions': regions,
        'categories': categories
    }
    if request.method == 'POST':
        try:
            models.Contact.objects.create(
                name=request.POST['name'],
                phone=request.POST['phone'],
                email=request.POST['email'],
                body=request.POST['body']
            )
        except:
            ...
    return render(request, 'front/contact.html', context)