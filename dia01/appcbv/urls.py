from django.urls import path
from .views import HelloView, CachorroListView, CachorroCreateView, CachorroDeleteView, CachorroUpdateView

urlpatterns = [
    path('',HelloView.as_view(), name="index"),
    path("listacachorro/", CachorroListView.as_view(), name='listacachorro'),
    path("criar/", CachorroCreateView.as_view(), name = "criarcachorro"),
    path("atualizar/<int:pk>", CachorroUpdateView.as_view(), name = "atualizarcachorro"),
    path("deletar/<int:pk>", CachorroDeleteView.as_view(), name = "deletarcachorro"),
]