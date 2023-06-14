window.onload = function() {
    const form = document.querySelector('form');
    const resultat = document.getElementById('resultat');
  
    // Créer un tableau pour stocker les résultats de conversion
    const conversions = [];
  
    form.addEventListener('submit', (event) => {
      event.preventDefault();
  
      const valeur = document.getElementById('valeur').value;
      const baseDepart = parseInt(document.getElementById('base-depart').value, 10);
      const baseArrivee = parseInt(document.getElementById('base-arrivee').value, 10);
  
      if (isNaN(parseInt(valeur, baseDepart))) {
        alert('Le message entré n\'est pas une valeur conforme.');
        return;
      }
  
      const nombreDecimal = parseInt(valeur, baseDepart);
      const messageConverti = nombreDecimal.toString(baseArrivee);
  
      conversions.push({
        valeur: valeur,
        baseDepart: baseDepart,
        baseArrivee: baseArrivee,
        resultat: messageConverti
      });
  
      // Afficher les résultats de conversion dans une liste
      resultat.innerHTML = '';
      for (let i = 0; i < conversions.length; i++) {
        const conversion = conversions[i];
        const listItem = document.createElement('li');
        listItem.textContent = `${conversion.valeur.toUpperCase()} (base ${conversion.baseDepart}) -> ${conversion.resultat.toUpperCase()} (base ${conversion.baseArrivee})`;
        resultat.appendChild(listItem);
      }
  
      // Effacer l'entrée de valeur
      document.getElementById('valeur').value = '';
    });
  }
  

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