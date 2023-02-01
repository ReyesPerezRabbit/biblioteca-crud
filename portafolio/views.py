from django.shortcuts import render
from .models import Project

# Create your views here.
def port_home(request):
    project = Project.objects.all()
    return render(request, 'por_home.html',{'project':project})