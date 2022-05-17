# Importar o TemplateView para criar páginas simples
from django.views.generic import TemplateView


# Create your views here.

# A classe PaginaInicial "extends" TemplateView
class PaginaInicial(TemplateView):
    # Toda classe filha do TemplateView precisa do
    # atributo abaixo para definir um template a ser renderizado
    #template_name = 'paginas/index2.html'
    template_name = 'paginas/home.html'
 
class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

class CadastraAtendimento(TemplateView):
    template_name = 'paginas/cadastraAtendimento.html'

class CadastraPessoa(TemplateView):
    template_name = 'paginas/cadastraPessoa.html'

class ConsultaPessoa(TemplateView):
    template_name = 'paginas/consultaPessoa.html'

class ConsultaAtendimento(TemplateView):
    template_name = 'paginas/consultaAtendimento.html'