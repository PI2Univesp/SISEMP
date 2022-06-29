import http from 'k6/http';

export const options = {
  thresholds: {
   http_req_failed: ['rate<0.01'], 
  },
}

export default function () {
  http.get('http://127.0.0.1:8000');
  
}