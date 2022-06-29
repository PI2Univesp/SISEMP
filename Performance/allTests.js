import http from 'k6/http';
import { check } from 'k6';
import { Trend, Rate, Counter, Gauge } from 'k6/metrics';
export const TrendRTT = new Trend('RTT');
export const RateContentOK = new Rate('Content OK');
export const GaugeContentSize = new Gauge('ContentSize');
export const CounterErrors = new Counter('Errors');

export const options = {
  vus: 10,
  duration: '30s',
  thresholds: {
    'RTT': ['p(99)<7000', 'p(70)<4000', 'avg<700', 'med<2000', 'min<500'],
    'ContentSize': ['value<20000'],
    'Errors': ['count<300'],
    // 90% of requests must finish within 3500ms, 95% within 4000, and 99.9% within 7s.
    http_req_duration: ['p(90) < 3500', 'p(95) < 4000', 'p(99.9)<7000'],
  },
};

export default function () {
  const res = http.get('https://sisemprc.herokuapp.com/home/');
  const contentOK = res.json('name') === 'Bert';

    TrendRTT.add(res.timings.duration);
    RateContentOK.add(contentOK);
    GaugeContentSize.add(res.body.length);

   
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
  




