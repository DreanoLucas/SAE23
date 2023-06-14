const toggle = document.getElementById('table');
const table = document.querySelector('table');
    
    toggle.addEventListener('click', () => {
      if (table.style.display === 'none') {
        table.style.display = '';
      } else {
        table.style.display = 'none';
      }
    });
    

const boutonsMasquer = document.querySelectorAll('h2');

for (let bouton of boutonsMasquer) {
      const section = bouton.parentNode;
      const elementsToHide = section.children;
    
      bouton.addEventListener('click', () => {
        section.classList.toggle('cacher-contenu');
        for (let element of elementsToHide) {
          if (element.tagName !== 'H1' && element.tagName !== 'H2') {
            element.classList.toggle('cacher-contenu');
          }
        }
      });
    }


const menuLateral = document.querySelector('.menu-lateral');
const boutonMenu = document.querySelector('#menu-toggle');
const contenuPage = document.querySelector('.contenu-page');

boutonMenu.addEventListener('click', () => {
  menuLateral.classList.toggle('menu-lateral-ouvert');
  contenuPage.classList.toggle('contenu-page-decale');
});