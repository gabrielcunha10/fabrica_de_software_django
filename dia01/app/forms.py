from django import forms
from .models import Usuario

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome','idade','email']