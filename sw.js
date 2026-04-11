// Service worker — network-first, with update notification support.
// skipWaiting() lets a new SW activate immediately, which triggers
// 'controllerchange' in the page so the update toast can be shown.
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', e => e.waitUntil(clients.claim()));
self.addEventListener('fetch', e => e.respondWith(fetch(e.request)));
