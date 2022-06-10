from django.shortcuts import render,redirect
from app.forms import PessoaForm, AtendimentoForm
from app.models import CadastrarPessoa, CadastrarAtendimento
import requests


def home(request):
    apiData = {}
    url = 'https://api.hgbrasil.com/weather?key=e390abc2'
    response = requests.get(url)
    apiData = response.json()
    return render(request, 'home.html', {'apiData': apiData})
    #return render(request, 'home.html')


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
        
        data['db'] = (CadastrarAtendimento.objects.filter(atendente__icontains=search) or CadastrarAtendimento.objects.filter(data__icontains=search) or CadastrarAtendimento.objects.filter(servico__icontains=search))
    else:
        data['db'] = CadastrarAtendimento.objects.all
    return render(request,'consultaAtendimento.html',data)


def create2(request):
    form = AtendimentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("consulta-atendimento")

"""" 
def testeApi(request):
    response = requests.get('https://viacep.com.br/ws/13401734/json/')
    apiData = response.json()
    return render(request, 'testeApi.html', {
        'logradouro': apiData['logradouro'],
        'complemento': apiData['complemento'],
        'bairro': apiData['bairro'],
        'localidade': apiData['localidade'],
        'uf': apiData['uf']
    })

def testeApi(request):
    apiData = {}
    if 'cep' in request.GET:
        cep = request.GET['cep']
        url = 'https://viacep.com.br/ws/%s/json/' % cep
        response = requests.get(url)
        apiData = response.json()
    return render(request, 'testeApi.html', {'apiData': apiData})
"""
