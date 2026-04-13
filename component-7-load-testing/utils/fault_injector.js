import http from 'k6/http';

export function setFault(config) {
    http.post('http://localhost:3000/fault', JSON.stringify(config), {
        headers: { 'Content-Type': 'application/json' },
    });
}