from django.urls import path
from . import views
from .views import listar_pessoas

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', listar_pessoas, name='listar_pessoas'),
]