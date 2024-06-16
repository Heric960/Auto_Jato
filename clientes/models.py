from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cpf = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.nome
    
class Carros(models.Model):
    carro = models.CharField(max_length=50)
    placa = models.CharField(max_length=50)
    ano = models.CharField(max_length=4)

    def __str__(self) -> str:
        return self.carro