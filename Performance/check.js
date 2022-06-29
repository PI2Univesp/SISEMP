//Checando se a requisição retornoa status 200, Texto na Home e Tamanho em bits do site.

import { check } from 'k6';
import http from 'k6/http';

export default function () {
  const res = http.get('http://127.0.0.1:8000');
  check(res, {
    'is status 200': (r) => r.status === 200,
  });

 check(res, {
    'verify homepage text': (r) =>
    r.body.includes('Bem-vindo ao Sistema'),
    
  });
  

  check(res, {
     "body size is 11637": (r) => r.body.length == 11637,
     });
}