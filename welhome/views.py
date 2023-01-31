from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


# vistas en la pagina

def well_home(request):
    return render(request, 'well_home.html')


def well_signup(request):
    if request.method == 'GET':
        return render(request, 'well_signup.html', {
            'Form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                # aqui te manda a la ruta cuando te registras
                return redirect('well_tasks')
            except IntegrityError:
                return render(request, 'well_signup.html', {
                    'Form': UserCreationForm,
                    "error": 'usuario ya existe'
                })
        return render(request, 'well_signup.html', {
            'Form': UserCreationForm,
            "error": 'Contraseñas no coinciden'
        })


def well_tasks(request):
     return render(request, 'well_tasks.html')

@login_required
def well_signout(request):
    logout(request)
    return redirect('well_home')


def well_signin(request):
    if request.method == 'GET':
        return render(request, 'well_signin.html', {
            'Form': AuthenticationForm
        })

    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
                return render(request, 'well_signin.html', {
            'Form': AuthenticationForm,
            'error' : 'username or password is incorrect'
        })
        else:
            login(request,user)
            return redirect('well_tasks')
