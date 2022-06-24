from django.db import models

# Create your models here.
class CadastrarPessoa(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.IntegerField()
    data = models.DateField(verbose_name="Data de Nascimento")
    email = models.CharField(max_length=150)
    telefone = models.IntegerField()
    cep = models.IntegerField()
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)

    def __str__(self):
        return "{}".format(self.cpf)


class CadastrarAtendimento(models.Model):
    
    cadastrarpessoa = models.ForeignKey(CadastrarPessoa, on_delete=models.PROTECT,verbose_name="CPF")
    
    

    servico_escolhas = (
        ("Orientação para MEI", "Orientação para MEI"),
        ("Consulta prévia de Localização", "Consulta prévia de Localização"),
        ("Registro, alteração e baixa do MEI", "Registro, alteração e baixa do MEI"),
        ("Emissão de boletos", "Emissão de boletos"),
        ("Orientação sobre renovação de alvará", "Orientação sobre renovação de alvará"),
        ("Orientação para emissão de NF", "Orientação para emissão de NF"),
    )

    servico = models.CharField(max_length=50, choices=servico_escolhas, blank=False, null=False)
    
    data = models.DateField()


    atendentes_escolhas = (
        ("Arande", "Arande"),
        ("Carlos", "Carlos"),
        ("Carolina", "Carolina"),
        ("Larissa", "Larissa"),
        ("Micael", "Micael"),
        ("Rafael", "Rafael"),
        ("Rodrigo", "Rodrigo"),
    )

    atendente = models.CharField(max_length=20, choices=atendentes_escolhas, blank=False, null=False)
