from django.shortcuts import render

from blog_app.models import Post


def blog(request):
    posts=Post.objects.all()
    return render(request, "blog_app/blog.html", {"posts": posts})
