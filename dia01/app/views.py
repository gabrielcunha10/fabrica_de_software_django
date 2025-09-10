from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

def home(request):
    return render(request, 'home.html')

def listar_pessoas(request):
    usuarios = Usuario.objects.all()
    return render(request, 'list.html', {'pessoas': usuarios})
