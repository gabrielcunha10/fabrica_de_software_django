from django.db import models

class Cachorro(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    raca = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
