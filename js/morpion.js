var plateau = document.getElementById("game-board");
var cells = plateau.getElementsByTagName("td");
var joueur = "X";

var markCell = function() {
  if (this.innerHTML !== "") {
    return;
  }
  this.innerHTML = joueur;
  this.style.color = (joueur === "X" ? "red" : "blue");
  joueur = (joueur === "X" ? "O" : "X");
  Victoire();
};

var Victoire = function() {
  for (var i = 0; i < 3; i++) {
    if (cells[i*3].innerHTML !== "" && cells[i*3].innerHTML === cells[i*3+1].innerHTML && cells[i*3+1].innerHTML === cells[i*3+2].innerHTML) {
      alert(cells[i*3].innerHTML + " a gagné!");
      resetGame();
      return;
    }
  }
  
  for (var i = 0; i < 3; i++) {
    if (cells[i].innerHTML !== "" && cells[i].innerHTML === cells[i+3].innerHTML && cells[i+3].innerHTML === cells[i+6].innerHTML) {
      alert(cells[i].innerHTML + " a gagné!");
      resetGame();
      return;
    }
  }
  
  if (cells[0].innerHTML !== "" && cells[0].innerHTML === cells[4].innerHTML && cells[4].innerHTML === cells[8].innerHTML) {
    alert(cells[0].innerHTML + " a gagné!");
    resetGame();
    return;
  } else if (cells[2].innerHTML !== "" && cells[2].innerHTML === cells[4].innerHTML && cells[4].innerHTML === cells[6].innerHTML) {
    alert(cells[2].innerHTML + " a gagné!");
    resetGame();
    return;
  }
  
  var egalite = true;
  for (var i = 0; i < cells.length; i++) {
    if (cells[i].innerHTML === "") {
      egalite = false;
      break;
    }
  }
  if (egalite) {
    alert("Match nul!");
    resetGame();
    return;
  }
};

var resetGame = function() {
  for (var i = 0; i < cells.length; i++) {
    cells[i].innerHTML = "";
    cells[i].style.color = "black";
  }
  joueur = "X";
};

for (var i = 0; i < cells.length; i++) {
  cells[i].addEventListener("click", markCell);
}