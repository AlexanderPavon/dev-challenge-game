from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('game/', views.game_view, name='game'),

    path('aboutus/', views.about_us, name='aboutus'),
    path('ranking/', views.ranking, name='ranking'),
    path('plantations/', views.plantations, name='plantations'),
    path('knowmore/', views.know_more, name='knowmore'),
]
