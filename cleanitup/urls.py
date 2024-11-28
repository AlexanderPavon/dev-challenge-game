from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cleanitup'

urlpatterns = [
    path('', views.index, name='index'),

    # Login/Logout URLs
    #path('login/', views.LoginView, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]