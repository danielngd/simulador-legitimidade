from django.db import models

class Produto(models.Model):
    codigo = models.IntegerField()
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=4)
    embalagens = models.CharField(max_length=4)
    comp = models.IntegerField()
    descricao = models.CharField(max_length=255)
    cpv = models.FloatField()

    def __str__(self) -> str:
        return "({}) {} | {}".format(self.codigo, self.nome, self.descricao)

class Estado(models.Model):
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=4)

    def __str__(self) -> str:
        return self.sigla

class Imposto(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.FloatField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "({}) {}".format(self.estado, self.nome)