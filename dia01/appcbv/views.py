from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Cachorro
class HelloView(View):
    def get(self, request):
        return HttpResponse("Boa tarde.")
class CachorroListView(ListView):
    model = Cachorro
    template_name = "lista.html"
    context_object_name = "cachorros"