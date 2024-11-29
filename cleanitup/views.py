from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404,redirect,render

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages





def index(request):
    return render(request, 'index.html')





def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario en la base de datos
            messages.success(request, '¡Tu cuenta ha sido creada exitosamente! Ahora puedes iniciar sesión.')
            return redirect('login')  # Redirige al login después del registro exitoso
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})