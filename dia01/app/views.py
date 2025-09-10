from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from django import forms
from .forms import PessoaForm

def home(request):
    return render(request, 'home.html')

def listar_pessoas(request):
    usuarios = Usuario.objects.all()
    return render(request, 'list.html', {'pessoas': usuarios})

def criar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'create.html', {'pessoa': form})