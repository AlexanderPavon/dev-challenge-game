from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404,redirect,render

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


from django.contrib import messages





def index(request):
    return render(request, 'index.html')