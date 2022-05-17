from django.urls import path

# Importa as views que a gente criou 
from .views import PaginaInicial, SobreView, CadastraAtendimento, CadastraPessoa, ConsultaPessoa, ConsultaAtendimento

# Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    # Todo path tem endereço, sua_view.as_view() e nome
    #path('', PaginaInicial.as_view(), name='index'),
    path('', PaginaInicial.as_view(), name='home'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('cadastraAtendimento/', CadastraAtendimento.as_view(), name='cadastraAtendimento'),
    path('cadastraPessoa/', CadastraPessoa.as_view(), name='cadastraPessoa'),
    path('consultaPessoa/', ConsultaPessoa.as_view(), name='consultaPessoa'),
    path('consultaAtendimento/', ConsultaPessoa.as_view(), name='consultaAtendimento'),
]
