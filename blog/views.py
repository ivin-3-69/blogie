from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post,Comment

def index(request):
    posts = Post.objects.all().order_by('-created_date')
    context = {
        "posts" : posts,
    }
    return render(request, "blog_index.html", context) 

def blog_category(request,category):
    posts = Post.objects.filter(categories__name__contains = category).order_by('-created_date')
    context = {
        "posts" : posts,
        "category" : category,
    }
    return render(request, "blog_category.html", context) 

def blog_detail(request, pkey):
    post = Post.objects.get(pk=pkey)
    comments = Comment.objects.filter(post=post)
    context = {
        "post" : post,
        "comments": comments,
    }
    return render(request, "blog_detail.html", context)