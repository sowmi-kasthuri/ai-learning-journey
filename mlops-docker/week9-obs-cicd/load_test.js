import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  vus: 20,
  duration: '2m',
};

export default function () {
  const payload = JSON.stringify({
    prompt: "hello from load test",
    model: "llama-3.1-8b-instant"
  });

  const params = {
    headers: { 'Content-Type': 'application/json' },
  };

  http.post('http://host.docker.internal:8000/generate', payload, params);
  sleep(1);
}
