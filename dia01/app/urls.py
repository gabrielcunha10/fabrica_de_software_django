from django.urls import path
from . import views
from .views import listar_pessoas
from .views import criar_pessoa

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', listar_pessoas, name='listar_pessoas'),
    path('criar/', criar_pessoa, name='criar_pessoa'),
]