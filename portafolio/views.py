from django.shortcuts import render

# Create your views here.
def port_home(request):
    return render(request, 'por_home.html')