from django.urls import path

from .views import CadastrarAtendimentoCreate, CadastrarPessoaCreate
from .views import AtendimentoList, PessoaList

# Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    path('cadastrar/CadastrarAtendimento/', CadastrarAtendimentoCreate.as_view(), name="cadastrar-atendimento"),
    path('cadastrar/CadastrarPessoa/', CadastrarPessoaCreate.as_view(), name="cadastrar-pessoa"),

    path('listar/pessoa/', PessoaList.as_view(), name='listar-pessoa'),
    path('listar/atendimento/', AtendimentoList.as_view(), name='listar-atendimento'),
]
