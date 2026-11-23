self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", (event) => {
  event.waitUntil((async () => {
    await caches.delete("mon-cacao-v2.0");
    await self.registration.unregister();
    const tabs = await self.clients.matchAll({type:"window"});
    await Promise.allSettled(tabs.filter((tab) => tab.url.startsWith(self.registration.scope)).map((tab) => tab.navigate(tab.url)));
  })());
});
