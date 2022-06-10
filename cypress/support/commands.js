Cypress.Commands.add('goToPage', () => {
    Cypress.on("uncaught:exception", (err, runnable) => {
        return false;
    });
    cy.viewport(1920,1080);
    cy.visit("/");
})

Cypress.Commands.add('cadastraPessoa', (data, cpf, nome, email, telefone, cep, cidade, estado) => {
    cy.get('a[href="/consulta-pessoa"]').click()
    cy.get('button[class="btn btn-secondary btn-lg btn-block"]').click()
    cy.get('input[name="data"]').type(data)
    cy.get('input[name="cpf"]').type(cpf)
    cy.get('input[name="nome"]').type(nome)
    cy.get('input[name="email"]').type(email)
    cy.get('input[name="telefone"]').type(telefone)
    cy.get('input[name="cep"]').type(cep)
    cy.get('input[name="cidade"]').type(cidade)
    cy.get('input[name="estado"]').type(estado)
})
