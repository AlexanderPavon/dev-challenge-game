from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Player, GameData
from .forms import PlayerRegistrationForm

def index(request):
    """Vista de página principal"""
    return render(request, 'index.html')




def about_us(request):
    return render(request, 'aboutus.html')

def ranking(request):
    return render(request, 'ranking.html')

def plantations(request):
    return render(request, 'plantations.html')

def know_more(request):
    return render(request, 'knowmore.html')



@require_http_methods(["GET", "POST"])
def register_view(request):
    """Vista de registro de usuario"""
    if request.method == 'POST':
        form = PlayerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Opcional: Iniciar sesión automáticamente después del registro
            # login(request, user)
            return redirect('cleanitup:login')
    else:
        form = PlayerRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

@require_http_methods(["GET", "POST"])
def login_view(request):
    """Vista de inicio de sesión"""
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('cleanitup:index')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    
    return render(request, 'login.html')

@login_required
def logout_view(request):
    """Vista de cierre de sesión"""
    logout(request)
    return redirect('cleanitup:index')

@login_required
def game_view(request):
    """Vista del juego con guardado de puntaje"""
    if request.method == 'POST':
        try:
            score = int(request.POST.get('score', 0))
            
            # Obtener o crear registro de GameData para el usuario actual
            game_data, created = GameData.objects.get_or_create(player=request.user)
            
            # Actualizar último puntaje
            game_data.last_score = score
            
            # Actualizar mejor puntaje si es necesario
            if score > game_data.best_score:
                game_data.best_score = score
            
            game_data.save()
            
            return JsonResponse({
                'success': True, 
                'message': 'Puntaje guardado exitosamente',
                'best_score': game_data.best_score
            })
        
        except Exception as e:
            return JsonResponse({
                'success': False, 
                'message': f'Error al guardar puntaje: {str(e)}'
            }, status=400)
    
    # Obtener mejor puntaje para mostrar en el juego
    game_data, _ = GameData.objects.get_or_create(player=request.user)
    
    return render(request, 'game.html', {'best_score': game_data.best_score})
