function showLoadingCursor() {
  document.body.classList.add("loading-cursor");
}


let darkModeSwitch = document.getElementById('darkModeSwitch');

darkModeSwitch.addEventListener('change', function() {
  if(this.checked) {
    document.body.classList.add('dark-mode');
  } else {
    document.body.classList.remove('dark-mode');
  }
});
const cardGrid = document.getElementById("card-grid");
const addCardButton = document.getElementById("add-card-button");

addCardButton.addEventListener("click", function() {
  // Create new card element
  const newCard = document.createElement("div");
  newCard.classList.add("card");
  newCard.innerHTML = `
    <img class="card-img-top" src="image.jpg" alt="Card image">
    <div class="card-body">
      <h4 class="card-title">New Card</h4>
      <p class="card-text">Card content goes here</p>
      <button class="btn btn-primary">Button</button>
    </div>
  `;

  // Append new card to the grid
  cardGrid.appendChild(newCard);
});


