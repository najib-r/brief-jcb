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

function myFunction() {
  let input, filter, found, table, tr, td, i, j;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("t-body");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td");
      for (j = 0; j < td.length; j++) {
          if (td[j].innerHTML.toUpperCase().indexOf(filter) > -1) {
              found = true;
          }
      }
      if (found) {
          tr[i].style.display = "";
          found = false;
      } else {
          tr[i].style.display = "none";
      }
  }
}

let input = document.getElementById("myInput");
input.addEventListener('search', myFunction)
input.addEventListener('keyup', function(e) {
  let input, filter, found, table, tr, td, i, j;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("t-body");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td");
      for (j = 0; j < td.length; j++) {
          if (td[j].innerHTML.toUpperCase().indexOf(filter) > -1) {
              found = true;
          }
      }
      if (found) {
          tr[i].style.display = "";
          found = false;
      } else {
          tr[i].style.display = "none";
      }
  }
  if (e.which === 13) {
    input.blur()
  }
})

let search = document.getElementById("searchBtn");
search.addEventListener('click', () => {
  input.blur();
})

function startLoading(page) {
  document.getElementById('loader').style.display = 'flex';
  document.querySelector('.pagination').style.top = '19px';
  setTimeout(function () {
    window.location.href = window.location.origin + `/${page}`;
  }, 200);
}

window.onpageshow = function() {
  document.getElementById('loader').style.display = 'none';
  document.querySelector('.pagination').style.top = '0';
};


let mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 500 || document.documentElement.scrollTop > 500) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}