// Minimal service worker — required for PWA installability.
// Strategy: network-first, no caching (content updates every push).
self.addEventListener('fetch', (event) => {
  event.respondWith(fetch(event.request));
});
