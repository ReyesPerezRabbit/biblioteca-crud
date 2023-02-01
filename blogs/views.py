from django.shortcuts import render

# Create your views here.
def blog_pu(request):
    return render(request, 'blogs_publi.html')