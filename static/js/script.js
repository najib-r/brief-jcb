window.addEventListener("load", () => {
  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("/static/sw.js");
  }
});

// Check to see if Media-Queries are supported
if (window.matchMedia) {
    // Check if the dark-mode Media-Query matches
    if(window.matchMedia('(prefers-color-scheme: dark)').matches){
      // Dark
      document.getElementById('themeColor').content = "#121212";
    }
}