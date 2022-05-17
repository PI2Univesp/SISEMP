from tokenize import Number
from django.db import models

# Create your models here.
class CadastroAtendimento(models.Model):
    nome = models.CharField(max_length=70)
    cpf = models.DecimalField(decimal_places=0, max_digits=13)
    dataNascimento = models.DecimalField(decimal_places=0, max_digits=8, verbose_name="Data de Nascimento") 
    telefone = models.DecimalField(decimal_places=0, max_digits=14)
    email = models.CharField(max_length=70)
    servico = models.CharField(max_length=225, verbose_name="Serviço")
    atendente = models.CharField(max_length=999)

