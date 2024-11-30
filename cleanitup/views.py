from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404,redirect,render
from .forms import PlayerForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages





def index(request):
    return render(request, 'index.html')



def register(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            # Guardar el jugador
            form.save()
            return redirect('cleanitup:login')  # Redirige a la página de inicio de sesión
    else:
        form = PlayerForm()
    
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Autenticar usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Iniciar sesión
            login(request, user)
            return redirect('cleanitup:home')  # Redirigir a la página de inicio o dashboard
        else:
            # Mostrar mensaje de error
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'login.html')