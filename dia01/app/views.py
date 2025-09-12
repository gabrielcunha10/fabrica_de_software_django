from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from django import forms
from .forms import PessoaForm
import requests

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

def deletar_pessoa(request, pk):
    pessoa = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('listar_pessoas')
    return render(request, 'confirmar_delete.html',{'pessoa': pessoa})

def atualizar_pessoa(request, pk):
    pessoa = Usuario.objects.get(pk=pk)
    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'create.html', {'pessoa': form})

def consultaCep(request):
    response = requests.get('https://viacep.com.br/ws/01001000/json/', verify=False)
    dadosEndereco = response.json()
    endereco = Usuario.objects.create(
        nome=dadosEndereco['logradouro'],
        idade=dadosEndereco['ibge'],
        email=dadosEndereco['bairro']
    )
    return HttpResponse(dadosEndereco['logradouro'])