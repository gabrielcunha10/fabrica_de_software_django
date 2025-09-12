from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Cachorro
from .forms import CachorroForm


class HelloView(View):
    def get(self, request):
        return HttpResponse("Boa tarde.")
class CachorroListView(ListView):
    model = Cachorro
    template_name = "lista.html"
    context_object_name = "cachorros"

class CachorroCreateView(CreateView):
    model = Cachorro
    form_class = CachorroForm
    template_name = "criarcachorro.html"
    success_url = reverse_lazy("listacachorro")

class CachorroUpdateView(UpdateView):
    model = Cachorro
    form_class = CachorroForm
    template_name = "criarcachorro.html"
    context_object_name = "atualizacachorro"
    success_url = reverse_lazy("listacachorro")

class CachorroDeleteView(DeleteView):
    model = Cachorro
    template_name = "deletarcachorro.html"
    context_object_name = "cachorro"
    success_url = reverse_lazy("listacachorro")
