from django.forms import ModelForm
from app.models import CadastrarPessoa, CadastrarAtendimento

# Create the form class.
class PessoaForm(ModelForm):
    class Meta:
        model = CadastrarPessoa
        fields = ['data','cpf','nome','email','telefone','cep','cidade','estado']

class AtendimentoForm(ModelForm):
    class Meta:
        model = CadastrarAtendimento
        fields = ['cadastrarpessoa','data', 'servico', 'atendente']