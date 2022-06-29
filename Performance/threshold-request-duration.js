//Limites aceitaveis no máximo 1% da requisições podem ter erro 
// 95% das requisições devem ocorrer em menos de 3.5s 

import http from 'k6/http';

export const options = {
  thresholds: {
   // 90% of requests must finish within 3500ms, 95% within 4000, and 99.9% within 7s.
   http_req_duration: ['p(90) < 3500', 'p(95) < 4000', 'p(99.9)<7000'],
   
  },
};

export default function () {
  http.get('http://127.0.0.1:8000');

}