listpre = document.querySelectorAll("pre")
fetch('python/bataille_navale.py')
    .then(response => response.text())
    .then( text => {
        pre = listpre[0];
        console.log(text)
        pre.textContent = text
    });
fetch('python/tools2.py')
  .then(response => response.text())
  .then( text => {
      pre = listpre[1];
      console.log(text)
      pre.textContent = text
    });
    
const menuLateral = document.querySelector('.menu-lateral');
const boutonMenu = document.querySelector('#menu-toggle');
const contenuPage = document.querySelector('.contenu-page');

boutonMenu.addEventListener('click', () => {
menuLateral.classList.toggle('menu-lateral-ouvert');
contenuPage.classList.toggle('contenu-page-decale');
});


const boutonsMasquer = document.querySelectorAll('h2');
console.log(boutonsMasquer)
for (let bouton of boutonsMasquer) {
      console.log(bouton)
      const section = bouton.parentNode;
      console.log(section)
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