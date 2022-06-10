/// <reference types="cypress" />
// import auth from "../support/appActions"
import faker from "@faker-js/faker";
faker.locale = 'pt_BR';


describe('Teste de Regressão SISEMP', () => {
    beforeEach(() => {
        cy.goToPage(); 
    });

    //Tela Home 

    it('Validar Texto Pagina Inicial', () => {
        cy.get('h1[class="display-3"]').contains('Bem-vindo ao Sistema')
    })

    it('Validar API Navbar - São Paulo, Temperatura', ()=>{
        cy.contains('div[class="container-fluid"]', 'São Paulo, Temperatura')
    })

    it('Validar Opções NavBar', () => {
        cy.get('div[class="container-fluid"]').should('contain', 'Página Principal')
        cy.get('div[class="container-fluid"]').should('contain','Pessoas')
        cy.get('div[class="container-fluid"]').should('contain','Atendimento')
        cy.get('div[class="container-fluid"]').should('contain','Sobre')
        cy.get('a[class="nav-link dropdown-toggle"]').click()
        cy.get('a[href="/consulta-atendimento"]').should('contain','Consultar')
        cy.get('a[href="/cadastrar-atendimento"]').should('contain','Cadastrar')
       
    })

    it('Validar Link Noticia 1', ()=>{
        cy.get('div[class="col-md-4"]').eq(0).should('contain', 'Notícias')
        cy.get('a[href="https://www.gruporioclarosp.com.br/2021/06/21/prefeito-gustavo-perissinotto-inaugura-sala-do-empreendedor/"]')
        .should('contain', 'Ver detalhes')
        .and('have.attr', 'href', 'https://www.gruporioclarosp.com.br/2021/06/21/prefeito-gustavo-perissinotto-inaugura-sala-do-empreendedor/')
    })

    it('Validar Link Noticia 2', ()=>{
        cy.get('div[class="col-md-4"]').eq(0).should('contain', 'Notícias')
        cy.contains('a[href="https://imprensa.rioclaro.sp.gov.br/?p=63929"]','Ver detalhes')
        cy.get('a[href="https://imprensa.rioclaro.sp.gov.br/?p=63929"]')
        .should('have.attr', 'href', 'https://imprensa.rioclaro.sp.gov.br/?p=63929')
        
    })

    it('Validar Link Noticia 3', ()=>{
        cy.get('div[class="col-md-4"]').eq(0).should('contain', 'Notícias')
        cy.contains('a[href="https://imprensa.rioclaro.sp.gov.br/?p=41425"]','Ver detalhes')
        cy.get('a[href="https://imprensa.rioclaro.sp.gov.br/?p=41425"]')
        .should('have.attr', 'href', 'https://imprensa.rioclaro.sp.gov.br/?p=41425')
        
    })


    //Tela Consulta Pessoa 
    
    it('Validar Cabeçalho Tabelda - Consultar Pessoa', () => {
        cy.get('a[href="/consulta-pessoa"]').click()
        cy.get('thead[class="thead-dark"]').should('contain', 'Nome')
        cy.get('thead[class="thead-dark"]').should('contain', 'CPF')
        cy.get('thead[class="thead-dark"]').should('contain', 'Email')
        cy.get('thead[class="thead-dark"]').should('contain', 'Telefone')
        cy.get('thead[class="thead-dark"]').should('contain', 'CEP')
        cy.get('thead[class="thead-dark"]').should('contain', 'Cidade')
        cy.get('thead[class="thead-dark"]').should('contain', 'Estado')
        cy.get('thead[class="thead-dark"]').should('contain', 'Data Nascimento')   
    })

    it('Pesquisando Pessoa Não Cadastrada', ()=>{
        cy.get('a[href="/consulta-pessoa"]').click()
        cy.get('input[id="search"]').click({force:true})
        cy.get('input[id="search"]').type('EsseUsuarioNãoExiste')
        cy.get('button[class="btn btn-secondary"]').click({force:true})
        cy.get('button[class="btn btn-secondary btn-lg btn-block"]').should('be.visible')
    })

    it('Pesquisando Pessoa Cadastrada', ()=>{
        const name = "cris" 
        cy.get('a[href="/consulta-pessoa"]').click()
        cy.get('input[id="search"]').click({force:true})
        cy.get('input[id="search"]').type(name)
        cy.get('button[class="btn btn-secondary"]').click({force:true})
        cy.get('button[class="btn btn-secondary btn-lg btn-block"]').should('be.visible')
        cy.get('tbody').should('contain', name)
    })

    //Tela Cadastra Pessoa 

    it('Cadastrar Pessoa', function (){
        cy.cadastraPessoa("16/01/1998",faker.random.numeric(13), faker.name.firstName(), faker.internet.email(), faker.random.numeric(11), faker.random.numeric(8), faker.address.cityName('pt_BR'), faker.address.state('pt_BR'));
        cy.get('input[name="nome"]').invoke('text').as('name');
        cy.get('input[value="Salvar"]').click({force: true})
    })

    it('Validando Cadastro realizado - Na tabela', function (){ 
        cy.get('a[href="/consulta-pessoa"]').click()
        cy.get('tbody').invoke('text').should('contain', this.name)
    })

    //Tela de Cadastra Atendimento 
    const cpf = '44917421896'
    it('Cadastrar Atendimento', ()=>{
        cy.get('div[class="container-fluid"]').click({force:true})
        cy.get('a[href="/cadastrar-atendimento"]').click({force:true})
        cy.get('select[id="id_cadastrarpessoa"]').select(cpf)
        cy.get('input[name="data"]').type('01/06/2022')
        cy.get('select[name="servico"]').select('Orientação para MEI')
        cy.get('select[name="atendente"]').select('Arande')
        cy.get('input[value="Cadastrar"]').click()

    })

    it('Validar Atendimento Cadastrado', function (){
        cy.get('div[class="container-fluid"]').click({force:true})
        cy.get('a[href="/consulta-atendimento"]').click({force:true})
        cy.get('tbody').should('contain', cpf)

    })

    //Tela Consulta Atendimento 

    it('Validar Cabeçalho Consulta Atendimento', function (){
        cy.get('div[class="container-fluid"]').click({force:true})
        cy.get('a[href="/consulta-atendimento"]').click({force:true})
        cy.get('thead[class="thead-dark"]').should('contain','CPF')
        cy.get('thead[class="thead-dark"]').should('contain','Data')
        cy.get('thead[class="thead-dark"]').should('contain','Serviço')
        cy.get('thead[class="thead-dark"]').should('contain','Atendente')

    })

    it('Validar Texto Tela Sobre', function (){
      cy.get('a[href="/sobre"]').click()
      cy.get('h1[class="display-3"]').should('contain', 'Sobre')
      cy.get('div[class="container"]').should('contain', 'Sistema desenvolvido pelos alunos da Universidade Virtual do Estado de São Paulo')

    })

    it('Validar Link Noticia 1 Tela Sobre', ()=>{
        cy.get('a[href="/sobre"]').click()
        cy.get('div[class="col-md-4"]').eq(0).should('contain', 'Notícias')
        cy.get('a[href="https://www.gruporioclarosp.com.br/2021/06/21/prefeito-gustavo-perissinotto-inaugura-sala-do-empreendedor/"]')
        .should('contain', 'Ver detalhes')
        .and('have.attr', 'href', 'https://www.gruporioclarosp.com.br/2021/06/21/prefeito-gustavo-perissinotto-inaugura-sala-do-empreendedor/')
    })

    it('Validar Link Noticia 2 Tela Sobre', ()=>{
        cy.get('a[href="/sobre"]').click()
        cy.get('div[class="col-md-4"]').eq(1).should('contain', 'Notícias')
        cy.contains('a[href="https://imprensa.rioclaro.sp.gov.br/?p=63929"]','Ver detalhes')
        cy.get('a[href="https://imprensa.rioclaro.sp.gov.br/?p=63929"]')
        .should('have.attr', 'href', 'https://imprensa.rioclaro.sp.gov.br/?p=63929')
        
    })

    it('Validar Link Noticia 3 Tela Sobre', ()=>{
        cy.get('a[href="/sobre"]').click()
        cy.get('div[class="col-md-4"]').eq(2).should('contain', 'Notícias')
        cy.contains('a[href="https://imprensa.rioclaro.sp.gov.br/?p=41425"]','Ver detalhes')
        cy.get('a[href="https://imprensa.rioclaro.sp.gov.br/?p=41425"]')
        .should('have.attr', 'href', 'https://imprensa.rioclaro.sp.gov.br/?p=41425')
        
    })


})