// Quintal de Jogos — guarda o jogo para abrir rápido e funcionar sem internet
const VERSION = 'quintal-v6';
const CORE = ['/', '/manifest.webmanifest', '/icon-192.png', '/icon-512.png', '/apple-touch-icon.png',
  ...['intro-fruit','intro-memory','intro-lights','res-0','res-1','res-2','sum-0','sum-1','sum-2','sum-empty','new-player'].map((k) => '/audio/' + k + '.mp3'),
  'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js'];
self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(VERSION).then((c) => Promise.all(CORE.map((u) => c.add(new Request(u, { mode: u.startsWith('http') ? 'no-cors' : 'same-origin' })).catch(() => {})))).then(() => self.skipWaiting()));
});
self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k !== VERSION).map((k) => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  // o vídeo não é guardado: vai direto pela rede, só quando a pessoa assiste
  if (new URL(req.url).pathname.startsWith('/video/apresentacao')) return;
  // páginas: tenta a rede primeiro (para pegar atualizações) e cai no que está guardado
  if (req.mode === 'navigate') {
    e.respondWith(fetch(req).then((r) => { const copy = r.clone(); caches.open(VERSION).then((c) => c.put('/', copy)); return r; })
      .catch(() => caches.match('/')));
    return;
  }
  // arquivos (three.js, fontes, ícones): usa o guardado e atualiza por trás
  e.respondWith(caches.match(req).then((hit) => {
    const net = fetch(req).then((r) => { if (r && (r.ok || r.type === 'opaque')) { const copy = r.clone(); caches.open(VERSION).then((c) => c.put(req, copy)); } return r; }).catch(() => hit);
    return hit || net;
  }));
});
