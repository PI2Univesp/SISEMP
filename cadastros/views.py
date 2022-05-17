from django.views.generic.edit import CreateView

from .models import CadastrarAtendimento, CadastrarPessoa

from django.urls import reverse_lazy

# Create your views here.
class CadastrarAtendimentoCreate(CreateView):
    model = CadastrarAtendimento
    fields = ["cpf","nome", "data"]
    template_name = "cadastros/cadastroAtendimento.html"
    success_url = reverse_lazy("home")


class CadastrarPessoaCreate(CreateView):
    model = CadastrarPessoa
    fields = ["cpf","nome","email","telefone","endereço","cep"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("home")  