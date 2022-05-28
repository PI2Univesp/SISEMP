from django.shortcuts import render,redirect
from app.forms import PessoaForm, AtendimentoForm
from app.models import CadastrarPessoa, CadastrarAtendimento

def home(request):
    return render(request, 'home.html')


def sobre(request):
    return render(request, 'sobre.html')


# Cadastro e Consulta Pessoas

def formPessoa(request):
    data={}
    data['form'] = PessoaForm()
    return render(request,'cadastrarPessoa.html',data)

def consultaPessoa(request):
    data={}
    search = request.GET.get('search')
    if search:
        data['db'] = (CadastrarPessoa.objects.filter(nome__icontains=search ) or CadastrarPessoa.objects.filter(cpf__icontains=search ))
    else:
        data['db'] = CadastrarPessoa.objects.all
    return render(request,'consultaPessoa.html',data)

def create(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("consulta-pessoa")


# Cadastro e Consulta Atendimento

def formAtendimento(request):
    data={}
    data['form'] = AtendimentoForm()
    return render(request,'cadastrarAtendimento.html',data)

def consultaAtendimento(request):
    data={}
   
    search = request.GET.get('search')
    if search:
        
        data['db'] = (CadastrarAtendimento.objects.filter(atendente__icontains=search) or CadastrarAtendimento.objects.filter(data__icontains=search))
    else:
        data['db'] = CadastrarAtendimento.objects.all
    return render(request,'consultaAtendimento.html',data)


def create2(request):
    form = AtendimentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("consulta-atendimento")


