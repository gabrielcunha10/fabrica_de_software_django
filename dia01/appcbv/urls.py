from django.urls import path
from .views import HelloView, CachorroListView

urlpatterns = [
    path('',HelloView.as_view(), name="index"),
    path("listacachorro/", CachorroListView.as_view(), name='listacachorro')
]