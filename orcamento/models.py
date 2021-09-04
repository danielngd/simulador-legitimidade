from django.db import models

class Produto:
    codigo = models.IntegerField()
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=4)
    embalagens = models.CharField(max_length=4)
    comp = models.IntegerField()
    descricao = models.CharField()
    cpv = models.FloatField()