// Check to see if Media-Queries are supported
if (window.matchMedia) {
    // Check if the dark-mode Media-Query matches
    if(window.matchMedia('(prefers-color-scheme: dark)').matches){
      // Dark
      document.getElementById('themeColor').content = "#121212";
    }
}

(function() {
  if('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/sw.js')
               .then(function(registration) {
               console.log('Service Worker Registered');
               return registration;
      })
      .catch(function(err) {
        console.error('Unable to register service worker.', err);
      });
      navigator.serviceWorker.ready.then(function(registration) {
        console.log('Service Worker Ready');
      });
    });
  }
})();
