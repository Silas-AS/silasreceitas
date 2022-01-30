from django.db import models
from datetime import datetime
from pessoas.models import Pessoa

class Receitas(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_de_preparo = models.TextField()
    tempo_de_preparo = models.IntegerField()
    rendimentos = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)
