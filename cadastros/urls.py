from django.urls import path

from .views import CadastrarAtendimentoCreate, CadastrarPessoaCreate


# Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    path('cadastro/atendimento/', CadastrarAtendimentoCreate.as_view(), name="cadastrar-atendimento"),
    path('cadastrar/CadastrarPessoa/', CadastrarPessoaCreate.as_view(), name="cadastrar-pessoa"),
]
