from django.urls import path

from .views import CadastroAtendimentoCreate

urlpatterns = [
    path('cadastro/atendimento', CadastroAtendimentoCreate.as_view(), name= "cadastroAtendimento"),
]
