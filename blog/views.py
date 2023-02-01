from django.shortcuts import render

# Create your views here.


def blog_publicaciones(request):
    return render(request, 'blog_posts.html')