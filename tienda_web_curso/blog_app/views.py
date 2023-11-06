from django.shortcuts import render

from blog_app.models import Categoria, Post


def blog(request):
    posts = Post.objects.all()
    return render(request, "blog_app/blog.html", {"posts": posts})


def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render(request, "blog_app/categorias.html", {"categoria": categoria, "posts": posts})
