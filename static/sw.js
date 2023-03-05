console.log('Hello from sw.js');

importScripts('https://storage.googleapis.com/workbox-cdn/releases/6.4.1/workbox-sw.js');

if (workbox) {
  console.log(`Yay! Workbox is loaded 🎉`);

  // workbox.precaching.precacheAndRoute([
  //   {
  //     "url": "/",
  //     "revision": "1"
  //   }
  // ]);

  workbox.routing.registerRoute(
    /\.(?:js|css)$/,
    new workbox.strategies.StaleWhileRevalidate()
  );

  workbox.routing.registerRoute(
    /^https:\/\/fonts\.googleapis\.com/,
    new workbox.strategies.StaleWhileRevalidate({
        cacheName: 'google-fonts-stylesheets',
    })
);

} else {
  console.log(`Boo! Workbox didn't load 😬`);
}