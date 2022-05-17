from django.db import models

# Create your models here.
class CadastrarAtendimento(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=50)
    data = models.DateField()

class CadastrarPessoa(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=11)
    endereço = models.CharField(max_length=50)
    cep = models.CharField(max_length=8)

    