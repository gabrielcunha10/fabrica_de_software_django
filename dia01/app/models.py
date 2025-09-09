from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.CharField()
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nome
