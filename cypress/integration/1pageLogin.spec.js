/// <reference types="cypress" />
// import auth from "../support/appActions"
import faker from "@faker-js/faker";
faker.locale = 'pt_BR';


describe('Teste de Regressão SISEMP', () => {
    it("Logando na Pagina",() => {
        cy.visit('https://sisemprc.herokuapp.com');
        cy.get('input[name="email"]').type('admin@gmail.com') 
        cy.get('input[type="password"]').type('admin')
        cy.get('input[type="checkbox"]').check()
        cy.get('button[type=submit]').click({force: true})
    });
});