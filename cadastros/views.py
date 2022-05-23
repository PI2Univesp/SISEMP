from django.views.generic.edit import CreateView

from django.views.generic.list import ListView

from .models import CadastrarAtendimento, CadastrarPessoa

from django.urls import reverse_lazy

# Create your views here.

########################### CADASTRAR ##########################
class CadastrarPessoaCreate(CreateView):
    model = CadastrarPessoa
    fields = ['data','cpf','nome','email','telefone','cep','cidade','estado','pais']
    template_name = "cadastros/form2.html"
    success_url = reverse_lazy("home")  

class CadastrarAtendimentoCreate(CreateView):
    model = CadastrarAtendimento
    fields = ['cadastrarpessoa', 'servico', 'atendente']

    template_name = "cadastros/form.html"
    success_url = reverse_lazy("home")




############################## LISTA ###############################

class PessoaList(ListView):
    model = CadastrarPessoa
    template_name = 'cadastros/listas/pessoa.html'

class AtendimentoList(ListView):
    model = CadastrarAtendimento
    template_name = 'cadastros/listas/atendimento.html'