from django.views.generic.edit import CreateView


from .models import CadastroAtendimento

from django.urls import reverse_lazy

# Create your views here.

class CadastroAtendimentoCreate(CreateView):
    model = CadastroAtendimento
    fields =['nome', 'cpf', 'dataNascimento', 'telefone', 'email', 'servico', 'atendente']
    template_name = 'registros/CadastroAtendimento.html'
    succes_url = reverse_lazy('home')



