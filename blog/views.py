from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post,Comment
from blog.forms import CommentForm
from django.http import HttpResponseRedirect

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
    
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                user_name=form.cleaned_data["user_name"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            return HttpResponseRedirect("http://127.0.0.1:8000/blog/2")

    comments = Comment.objects.filter(post=post)
    context = {
        "post" : post,
        "comments": comments,
        "form" : form,
    }
    return render(request, "blog_detail.html", context)