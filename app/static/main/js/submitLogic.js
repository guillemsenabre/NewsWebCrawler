text = document.getElementById("mainTextContainer");
inputBox = document.getElementById("inputBox");
searchContainer = document.getElementById("searchBarContainer");
submitBtn = document.getElementById("searchBtn");

let isVisible = true;

//If the button is clicked, fetch data (using arrow function)
submitBtn.addEventListener('click', () => {
  query = inputBox.value;
  if (query !== ''){
    fadeOut();
  }
});

//If the user press enter key (13), fetch data (using anonymous function)
inputBox.addEventListener('keydown', (e) => {
  query = inputBox.value;
  if (e.keyCode === 13 && query !== '') {
    fadeOut();
  }
});



// Applies a "fade out" transition (class="disappear") 
//to the search bar and text 
function fadeOut () {
  text.classList.add('disappear');
  searchContainer.classList.add('disappear')
}