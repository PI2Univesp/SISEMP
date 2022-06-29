import http from 'k6/http';
import { Trend, Rate, Counter, Gauge } from 'k6/metrics';

export const TrendRTT = new Trend('RTT');
export const RateContentOK = new Rate('Content OK');
export const GaugeContentSize = new Gauge('ContentSize');
export const CounterErrors = new Counter('Errors');
export const options = {
  thresholds: {
    'RTT': ['p(99)<7000', 'p(70)<4000', 'avg<700', 'med<2000', 'min<500'],
    'ContentSize': ['value<20000'],
    'Errors': ['count<300'],
  },
};

export default function () {
  const res = http.get('http://127.0.0.1:8000');
  const contentOK = res.json('name') === 'Bert';

  TrendRTT.add(res.timings.duration);
  RateContentOK.add(contentOK);
  GaugeContentSize.add(res.body.length);

}